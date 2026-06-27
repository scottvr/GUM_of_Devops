const fs = require('fs');
const path = require('path');
const { chromium } = require('../node_modules/playwright');

const PAGE_URL = 'file:///Users/bundle-tron9k/GUM_of_Devops/DORA/gum-graph/index.html';
const OUT_DIR = '/private/tmp/gum-audit';

(async () => {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 2200 } });

  await page.goto(PAGE_URL, { waitUntil: 'domcontentloaded' });

  const report = await page.evaluate(() => {
    const issues = [];
    const add = (kind, selector, message) => issues.push({ kind, selector, message });

    const hasText = (v) => typeof v === 'string' && v.trim().length > 0;

    const controlRows = Array.from(document.querySelectorAll('.control-row'));
    controlRows.forEach((row, idx) => {
      const input = row.querySelector('input[type="range"]');
      const label = row.querySelector('.control-label');
      const value = row.querySelector('.control-value');
      const sel = `.control-row:nth-of-type(${idx + 1})`;
      if (!input) add('missing_input', sel, 'Control row has no range input.');
      if (!label || !hasText(label.textContent)) add('missing_label', sel, 'Control row has no visible label text.');
      if (!value || !hasText(value.textContent)) add('missing_value', sel, 'Control row has no displayed value text.');

      if (input) {
        const id = input.id ? '#' + input.id : sel + ' input[type=range]';
        const aria = input.getAttribute('aria-label') || '';
        if (!hasText(aria)) add('missing_aria', id, 'Range input missing aria-label.');

        const hasHelp = hasText(input.getAttribute('title') || '') || hasText(input.getAttribute('aria-description') || '');
        if (!hasHelp) add('missing_help', id, 'Range input has no title or aria-description guidance.');
      }
    });

    const valueElements = [
      '#score-value', '#ticker-pinst', '#ticker-preal', '#ticker-tdr', '#ticker-df-policy', '#ticker-df-eff',
      '#val-DF', '#val-LT', '#val-CFR', '#val-MTTR', '#val-M', '#val-U', '#val-Cm', '#val-E', '#val-TDR',
      '#val-R', '#val-V', '#val-lam', '#val-alpha', '#val-beta', '#tdr-rate'
    ];

    valueElements.forEach((id) => {
      const el = document.querySelector(id);
      if (!el) {
        add('missing_value_element', id, 'Expected value element not found.');
        return;
      }
      if (!hasText(el.textContent)) {
        add('empty_value_element', id, 'Value element exists but has no text.');
      }
    });

    const allSelects = Array.from(document.querySelectorAll('select'));
    allSelects.forEach((sel) => {
      const id = sel.id;
      if (!id) {
        add('missing_select_id', 'select', 'Select missing id for labeling.');
        return;
      }
      const explicitLabel = document.querySelector(`label[for="${id}"]`);
      const aria = sel.getAttribute('aria-label');
      if (!explicitLabel && !hasText(aria)) {
        add('missing_select_label', '#' + id, 'Select has no associated label or aria-label.');
      }
    });

    const allButtons = Array.from(document.querySelectorAll('button'));
    allButtons.forEach((btn, idx) => {
      const text = (btn.textContent || '').trim();
      const aria = (btn.getAttribute('aria-label') || '').trim();
      if (!text && !aria) add('missing_button_name', `button:nth-of-type(${idx + 1})`, 'Button has no text or aria-label.');
    });

    const baseline = document.querySelector('#baseline-compare');
    if (!baseline || !hasText(baseline.textContent)) {
      add('missing_baseline_text', '#baseline-compare', 'Baseline card has no readable text.');
    }

    const banner = document.querySelector('#df-dynamics-banner');
    if (!banner || !hasText(banner.textContent)) {
      add('missing_df_banner_text', '#df-dynamics-banner', 'DF assumptions banner missing or empty.');
    }

    const tooltipless = Array.from(document.querySelectorAll('input[type="range"]')).filter((el) => {
      return !hasText(el.getAttribute('title') || '') && !hasText(el.getAttribute('aria-description') || '');
    }).map((el) => '#' + el.id);

    return {
      controlRows: controlRows.length,
      selects: allSelects.length,
      buttons: allButtons.length,
      tooltipless,
      issues,
    };
  });

  await page.screenshot({ path: path.join(OUT_DIR, 'gum-home.png'), fullPage: true });

  const jsonPath = path.join(OUT_DIR, 'display-audit-report.json');
  fs.writeFileSync(jsonPath, JSON.stringify(report, null, 2));

  await browser.close();

  console.log('Display audit report saved:', jsonPath);
  console.log(JSON.stringify(report, null, 2));

  if (report.issues.length) {
    process.exitCode = 2;
  }
})();
