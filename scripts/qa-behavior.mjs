import { webkit, firefox } from 'playwright';
const BASE = 'http://localhost:4323';
for (const [name, engine] of Object.entries({ webkit, firefox })) {
  const browser = await engine.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto(BASE + '/', { waitUntil: 'networkidle' });
  const w1 = await page.textContent('[data-cycling-word]');
  await page.waitForTimeout(4000);
  const w2 = await page.textContent('[data-cycling-word]');
  console.log(`${name} typewriter: "${w1.trim()}" -> "${w2.trim()}" ${w1 !== w2 ? 'CYCLING ✓' : 'STUCK ✗'}`);
  // FAQ: click second question, panel should open
  const item = page.locator('[data-faq-item]').nth(1);
  await item.locator('[data-faq-button]').click();
  await page.waitForTimeout(400);
  const open = await item.getAttribute('data-open');
  console.log(`${name} FAQ toggle: ${open === 'true' ? 'OPENS ✓' : 'BROKEN ✗'}`);
  // reveal failsafe: after 3.5s nothing should still carry .pre
  await page.waitForTimeout(3500);
  const hidden = await page.evaluate(() => document.querySelectorAll('[data-reveal].pre').length);
  console.log(`${name} reveal failsafe: ${hidden} still hidden ${hidden === 0 ? '✓' : '✗'}`);
  // contact prefill
  await page.goto(BASE + '/contact/?email=test%40example.com', { waitUntil: 'networkidle' });
  const val = await page.inputValue('input[name="email"]');
  console.log(`${name} contact prefill: "${val}" ${val === 'test@example.com' ? '✓' : '✗'}`);
  await browser.close();
}
