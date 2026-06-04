/* Reading progress bar */
(function() {
  function updateProgress() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    var bar = document.querySelector('.progress-bar');
    if (bar) bar.style.width = scrolled + '%';
  }
  window.addEventListener('scroll', updateProgress);
  document.addEventListener('DOMContentLoaded', function() {
    var bar = document.createElement('div');
    bar.className = 'progress-bar';
    bar.style.width = '0%';
    document.body.appendChild(bar);
    updateProgress();
  });
})();

/* (Apple.com 風格) 不再注入 sidebar 內按鈕
   漢堡按鈕 = 唯一 toggle, 點 logo 不回首頁
   「⌂ 回首頁」按鈕由 lesson-header 模板在內容區頂部提供 */

/* 在每個章節頁 .lesson-header 內頂部加一個「⌂ 回首頁」按鈕
   老大需求: Apple.com 風格, 每個章節最頂部有回首頁按鈕
   注意: 跳過首頁 (/) 跟附錄/intro 等非章節頁 (沒 .lesson-header) */
(function() {
  function addHomeToLessonHeader() {
    var header = document.querySelector('.md-content .lesson-header');
    if (!header) return;  // 首頁/附錄/intro 沒 lesson-header, 跳過
    if (header.querySelector('.lesson-home-btn')) return;  // 避免重複

    var logoHref = document.querySelector('a.md-header__button.md-logo');
    var siteRoot = logoHref ? logoHref.getAttribute('href') : './';
    // 確保是絕對路徑 (含 /)
    if (siteRoot === '.' || siteRoot === '') siteRoot = './';
    // 從 logo href 推回網站根 (logo 永遠指向首頁)
    // mkdocs 內 logo href 通常是 "." 或 ".." 或 "/"
    // 統一: 如果不是以 / 開頭, 改用 ./
    if (!siteRoot.startsWith('/') && !siteRoot.startsWith('http')) {
      siteRoot = './';
    }

    var btn = document.createElement('a');
    btn.href = siteRoot;
    btn.className = 'lesson-home-btn';
    btn.setAttribute('aria-label', '回首頁');
    btn.title = '回首頁';
    btn.innerHTML =
      '<span class="lesson-home-btn__icon" aria-hidden="true">⌂</span>' +
      '<span class="lesson-home-btn__text">回首頁</span>';

    // 插到 lesson-header 最前面 (在 .chapter-tag / h1 之上)
    header.insertBefore(btn, header.firstChild);
  }

  // 三重保險 (含 MutationObserver 處理 SPA / 慢載入)
  function tryInject() {
    addHomeToLessonHeader();
  }
  document.addEventListener('DOMContentLoaded', tryInject);
  window.addEventListener('load', tryInject);

  if (typeof MutationObserver !== 'undefined') {
    var observer = new MutationObserver(function() {
      addHomeToLessonHeader();
    });
    observer.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function() { observer.disconnect(); }, 10000);
  }
})();
