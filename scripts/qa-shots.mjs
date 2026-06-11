import { webkit } from 'playwright';
const browser = await webkit.launch();
for (const [w, h, name] of [[1440, 900, 'desktop'], [375, 812, 'mobile']]) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  await page.goto('http://localhost:4323/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(3500);
  await page.screenshot({ path: `/tmp/v10-qa-webkit-${name}.png`, fullPage: true });
  await page.close();
}
await browser.close();
console.log('done');
