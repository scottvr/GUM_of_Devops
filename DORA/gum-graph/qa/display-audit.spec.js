const { test, expect } = require('@playwright/test');

const PAGE_URL = 'file:///Users/bundle-tron9k/GUM_of_Devops/DORA/gum-graph/index.html';

function hasText(v) {
  return typeof v === 'string' && v.trim().length > 0;
}

test('displayed values have understandable labels and controls expose intent', async ({ page }) => {
  await page.goto(PAGE_URL);
  await page.waitForLoadState('domcontentloaded');

  const report = await page.evaluate(() => {
    const issues = [];

    const add = (kind, selector, message) => issues.push({ kind, selector, message });

    const controlRows = Array.from(document.querySelectorAll('.control-row'));
    controlRows.forEach((row) => {
      const input = row.querySelector('input[type="range"]');
      const label = row.querySelector('.control-label');
      const value = row.querySelector('.control-value');
      if (!input) add('missing_input', '.control-row', 'Control row has no range input.');
      if (!label || !label.textContent.trim()) add('missing_label', '.control-row', 'Control row has no visible label text.');
      if (!value || !value.textContent.trim()) add('missing_value', '.control-row', 'Control row has no displayed value text.');

      if (input) {
        const aria = input.getAttribute('aria-label') || '';
        if (!aria.trim()) add('missing_aria', '#' + input.id, 'Range input missing aria-label.');

        const hasHelp = (input.getAttribute('title') || '').trim().length > 0 ||
          (input.getAttribute('aria-description') || '').trim().length > 0;
        if (!hasHelp) add('missing_help', '#' + input.id, 'Range input has no title/aria-description guidance.');
      }
    });

    const tickerPairs = Array.from(document.querySelectorAll('.sim-ticker > div'));
    tickerPairs.forEach((box, i) => {
      const label = box.querySelector('.ticker-label');
      const valueSpans = Array.from(box.querySelectorAll('span')).filter(s => !s.classList.contains('ticker-label'));
      if (!label || !label.textContent.trim()) add('missing_ticker_label', `.sim-ticker > div:nth-child(${i + 1})`, 'Ticker box missing label.');
      if (!valueSpans.length || !valueSpans.some(s => s.textContent.trim())) {
        add('missing_ticker_value', `.sim-ticker > div:nth-child(${i + 1})`, 'Ticker box missing displayed value.');
      }
    });

    const allButtons = Array.from(document.querySelectorAll('button'));
    allButtons.forEach((btn) => {
      const text = (btn.textContent || '').trim();
      const aria = (btn.getAttribute('aria-label') || '').trim();
      if (!text && !aria) add('missing_button_name', 'button', 'Button has no text or aria-label.');
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

    const compare = document.getElementById('baseline-compare');
    if (!compare || !compare.textContent.trim()) {
      add('missing_baseline_compare', '#baseline-compare', 'Current vs Baseline card has no readable text.');
    }

    return {
      controlRows: controlRows.length,
      tickerBoxes: tickerPairs.length,
      buttons: allButtons.length,
      selects: allSelects.length,
      issues,
    };
  });

  console.log('\n--- Display Audit Report ---');
  console.log(JSON.stringify(report, null, 2));

  expect(report.controlRows).toBeGreaterThan(0);
  expect(report.tickerBoxes).toBeGreaterThan(0);
  expect(report.issues, `Found semantic labeling issues:\n${JSON.stringify(report.issues, null, 2)}`).toEqual([]);
});
