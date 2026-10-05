// Stampa in PDF A4 una pagina HTML con Chromium (Playwright), con numeri di pagina a piè di pagina.
// Uso: node strumenti/stampa_pdf.js input.html output.pdf
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const [input, output] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
  await page.pdf({
    path: output,
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:8px;color:#78716c;text-align:center;font-family:sans-serif;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '22mm', bottom: '20mm', left: '18mm', right: '18mm' },
  });
  await browser.close();
})();
