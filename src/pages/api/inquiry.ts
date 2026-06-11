import type { APIRoute } from 'astro';

export const prerender = false;

// Contact form → Notion "Web Inquiries" database.
// Honeypot: bots that fill the hidden "website" field get a fake success.

const NOTION_TOKEN = import.meta.env.NOTION_TOKEN;
const NOTION_DATABASE_ID = import.meta.env.NOTION_DATABASE_ID;

export const POST: APIRoute = async ({ request, redirect }) => {
  let form: FormData;
  try {
    form = await request.formData();
  } catch {
    return redirect('/contact?error=1', 303);
  }

  const honeypot = String(form.get('website') ?? '');
  const name = String(form.get('name') ?? '').trim();
  const email = String(form.get('email') ?? '').trim();
  const company = String(form.get('company') ?? '').trim();
  const message = String(form.get('message') ?? '').trim();

  if (honeypot) return redirect('/contact?sent=1', 303); // bot: pretend success
  if (!name || !email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    return redirect('/contact?error=1', 303);
  }

  const clip = (s: string, n: number) => s.slice(0, n);

  const res = await fetch('https://api.notion.com/v1/pages', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${NOTION_TOKEN}`,
      'Notion-Version': '2022-06-28',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      parent: { database_id: NOTION_DATABASE_ID },
      properties: {
        Name: { title: [{ text: { content: clip(name, 200) } }] },
        Email: { email: clip(email, 200) },
        Company: { rich_text: company ? [{ text: { content: clip(company, 200) } }] : [] },
        Message: { rich_text: message ? [{ text: { content: clip(message, 1900) } }] : [] },
        Source: { select: { name: 'Website Form' } },
      },
    }),
  });

  if (!res.ok) {
    console.error('Notion write failed', res.status, await res.text());
    return redirect('/contact?error=1', 303);
  }

  return redirect('/contact?sent=1', 303);
};
