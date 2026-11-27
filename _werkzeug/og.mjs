// Rendert img/og.jpg (1200×630) aus _werkzeug/og.html – headless, kein sichtbares Fenster.
// Aufruf im Repo-Root:  node _werkzeug/og.mjs
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const require = createRequire('C:/Users/phili/Motocross/worktrees/n-int/package.json');
const { chromium } = require('playwright-core');
const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const QUELLE = process.env.MX_SIEGER_OG || 'C:/Users/phili/Motocross/abnahme/mxroyale/bild-turnier/sieger_aktuell/B02.png'; // Bild-Turnier-Sieger (Blender-Render)

const vorlage = fs.readFileSync(path.join(ROOT, '_werkzeug/og.html'), 'utf8').replace('QUELLE', pathToFileURL(QUELLE).href);
const tmpHtml = path.join(ROOT, '_werkzeug/og.tmp.html');
fs.writeFileSync(tmpHtml, vorlage);
const SHELL = 'C:/Users/phili/AppData/Local/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-win64/chrome-headless-shell.exe';
const browser = await chromium.launch({ headless: true, ...(fs.existsSync(SHELL) ? { executablePath: SHELL } : {}) });
try {
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  await page.goto(pathToFileURL(tmpHtml).href);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const ziel = path.join(ROOT, 'img/og.jpg');
  await page.screenshot({ path: ziel + '.tmp.jpg', type: 'jpeg', quality: 86 });
  fs.renameSync(ziel + '.tmp.jpg', ziel);
  console.log('ok img/og.jpg', fs.statSync(ziel).size >> 10, 'KB');
} finally {
  await browser.close();
  fs.rmSync(tmpHtml, { force: true });
}
