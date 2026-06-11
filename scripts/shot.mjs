// Headless screenshot harness for the fidelity loop.
// Usage: node scripts/shot.mjs <url> <outfile> [width] [height] [scrollY] [fullPage]
import { chromium } from 'playwright';

const [url, out, w = '1440', h = '900', scrollY = '0', fullPage = ''] = process.argv.slice(2);

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: +w, height: +h } });
await page.goto(url, { waitUntil: 'networkidle' });
if (+scrollY) {
  await page.evaluate((y) => window.scrollTo(0, y), +scrollY);
  await page.waitForTimeout(400);
}
await page.waitForTimeout(300);
await page.screenshot({ path: out, fullPage: fullPage === 'full' });
await browser.close();
console.log(`saved ${out}`);
