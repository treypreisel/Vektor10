import { chromium } from 'playwright';
import { readFileSync, writeFileSync, unlinkSync } from 'fs';

const logoDark = readFileSync('../Brand/V10_Logo_Dark_Color.svg', 'utf8');
const browser = await chromium.launch();

// --- OG image 1200x630 ---
const og = `<!doctype html><html><head><style>
@font-face { font-family: 'Geist Mono'; src: url('node_modules/@fontsource/geist-mono/files/geist-mono-latin-600-normal.woff2') format('woff2'); font-weight: 600; }
@font-face { font-family: 'Geist Mono'; src: url('node_modules/@fontsource/geist-mono/files/geist-mono-latin-500-normal.woff2') format('woff2'); font-weight: 500; }
* { margin: 0; box-sizing: border-box; }
body { width: 1200px; height: 630px; background: #F0EEE5; font-family: 'Geist Mono', monospace; position: relative; overflow: hidden;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 48px; }
.noise { position: absolute; inset: 0; background: url('public/noise.png'); opacity: .14; }
.logo svg { width: 470px; height: auto; display: block; position: relative; }
.eyebrow { position: relative; font-size: 23px; font-weight: 600; letter-spacing: .14em; color: #2E926C; }
.dither { position: absolute; left: 0; right: 0; bottom: 0; height: 52px;
  background: url('public/dither-green-bone.png'); background-size: auto 100%; background-repeat: repeat-x; image-rendering: pixelated; }
.url { position: absolute; top: 36px; right: 44px; font-size: 19px; font-weight: 500; color: #141413; opacity: .55; letter-spacing: .06em; }
</style></head><body>
  <div class="noise"></div>
  <div class="url">VEKTOR10.COM</div>
  <div class="logo">${logoDark}</div>
  <div class="eyebrow">&lt; THE 1ST FULL-SUITE CHATGPT COMMERCE AGENCY &gt;</div>
  <div class="dither"></div>
</body></html>`;
writeFileSync('og-render.html', og);
let page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 2 });
await page.goto(`file://${process.cwd()}/og-render.html`);
await page.waitForTimeout(600);
await page.screenshot({ path: 'public/og-default.jpg', type: 'jpeg', quality: 88 });
await page.close();
unlinkSync('og-render.html');

// --- PNG icons: inline svg, no external refs ---
for (const [size, pad, out, bg, omit] of [
  [64, 2, 'public/favicon-32.png', 'transparent', true],
  [180, 24, 'public/apple-touch-icon.png', '#F0EEE5', false],
]) {
  const p = await browser.newPage({ viewport: { width: size, height: size } });
  const inner = size - pad * 2;
  await p.setContent(`<body style="margin:0;width:${size}px;height:${size}px;background:${bg};display:flex;align-items:center;justify-content:center">
    <div style="width:${inner}px">${logoDark.replace('<svg ', '<svg style="width:100%;height:auto;display:block" ')}</div>
  </body>`);
  await p.waitForTimeout(200);
  await p.screenshot({ path: out, omitBackground: omit });
  await p.close();
}
await browser.close();
console.log('rendered');
