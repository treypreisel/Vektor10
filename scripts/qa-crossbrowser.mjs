import { chromium, webkit, firefox } from 'playwright';
const PAGES = ['/', '/about/', '/blog/', '/blog/emarketer-openai-ad-target/', '/contact/', '/terms/', '/privacy/'];
const ENGINES = { chromium, webkit, firefox };
const BASE = 'http://localhost:4323';
for (const [name, engine] of Object.entries(ENGINES)) {
  const browser = await engine.launch();
  for (const vp of [{w:1440,h:900},{w:375,h:812}]) {
    const ctx = await browser.newContext({ viewport: { width: vp.w, height: vp.h } });
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    for (const p of PAGES) {
      errors.length = 0;
      const resp = await page.goto(BASE + p, { waitUntil: 'networkidle' });
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      const status = resp.status();
      const flag = (status !== 200 || overflow > 1 || errors.length) ? ' <-- ISSUE' : '';
      console.log(`${name} ${vp.w}px ${p} status=${status} overflowX=${overflow}px errors=${errors.length}${flag}`);
      if (errors.length) errors.forEach(e => console.log('   ERR:', e.slice(0,200)));
    }
    await ctx.close();
  }
  await browser.close();
}
