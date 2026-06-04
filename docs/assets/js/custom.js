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
   注意: 跳過首頁 (/) 跟附錄/intro 等非章節頁 (沒 .lesson-header)

   重要: href 必須是 GitHub Pages 部署的絕對路徑 /python-learning-site/
   因為 GitHub Pages 站點部署在 https://.../python-learning-site/ 子路徑
   從任何子目錄 (chapter0X_setup/01-why-python/) 用 ./ 都會跳到同層而非根
   用 /python-learning-site/ 是最穩的「回首頁」寫法 */
(function() {
  function addHomeToLessonHeader() {
    var header = document.querySelector('.md-content .lesson-header');
    if (!header) return;  // 首頁/intro 沒 lesson-header, 跳過
    if (header.querySelector('.lesson-home-btn')) return;  // 避免重複

    // 動態計算回首頁的相對路徑
    // mkdocs material 已經把 logo href 算成正確的相對路徑 (例 chapter0X_setup/01-why-python/ 的 logo href=../..)
    // 從 logo href 拿, 自動處理所有子目錄層級, 不需要自己算
    var logoEl = document.querySelector('a.md-header__button.md-logo');
    var homeHref = './';  // fallback
    if (logoEl) {
      var href = logoEl.getAttribute('href');
      // mkdocs 給的 href 一定是 . 或 ./ 或 ../ 開頭的相對路徑
      // 如果是 . 開頭, 我們要的是 logo 指向的目標 (首頁), 保留原樣
      if (href && href !== '') {
        homeHref = href;
      }
    }

    var btn = document.createElement('a');
    btn.href = homeHref;
    btn.className = 'lesson-home-btn';
    btn.setAttribute('aria-label', '回首頁');
    btn.title = '回首頁';
    btn.innerHTML =
      '<span class="lesson-home-btn__icon" aria-hidden="true">←</span>' +
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
