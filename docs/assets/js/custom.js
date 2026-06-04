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

/* ---------- Sidebar splitter: 桌面可拖動調整寬度 ---------- */
/* 老大需求 2026-06-04:
   - 桌面 ≥ 76.25em: 中間 5px splitter, 鼠標拖動改 sidebar 寬度
   - 範圍: 12rem ~ 28rem
   - localStorage 記住使用者選擇 (key: 'pl-sidebar-width')
   - 手機 < 76.25em: 不注入 (維持漢堡 drawer)
   - 注意: mkdocs 預設 .md-main__inner 是 display: flex, splitter 放在 flex 子元素 */
(function() {
  var STORAGE_KEY = 'pl-sidebar-width';
  var MIN_PX = 192;   // 12rem (16px 字)
  var MAX_PX = 448;   // 28rem

  function initSplitter() {
    // 1. 只在桌面 (≥ 76.25em) 注入
    if (window.innerWidth < 76.25 * 16) return;

    // 2. 找 sidebar 跟 main 容器
    var sidebar = document.querySelector('.md-main__inner > .md-sidebar--primary');
    if (!sidebar) return;
    var main = sidebar.parentElement;
    if (!main) return;

    // 3. 注入 splitter (在 sidebar 之後)
    if (main.querySelector('.sidebar-splitter')) return;  // dedupe
    var splitter = document.createElement('div');
    splitter.className = 'sidebar-splitter';
    splitter.setAttribute('role', 'separator');
    splitter.setAttribute('aria-orientation', 'vertical');
    splitter.setAttribute('aria-label', '拖動調整側邊欄寬度');
    sidebar.parentNode.insertBefore(splitter, sidebar.nextSibling);

    // 4. 從 localStorage 還原寬度
    var saved = parseInt(localStorage.getItem(STORAGE_KEY), 10);
    if (saved && saved >= MIN_PX && saved <= MAX_PX) {
      document.documentElement.style.setProperty('--sidebar-width', saved + 'px');
    }

    // 5. 拖動邏輯
    var dragging = false;
    var startX = 0;
    var startWidth = 0;

    splitter.addEventListener('mousedown', function(e) {
      dragging = true;
      startX = e.clientX;
      startWidth = sidebar.getBoundingClientRect().width;
      splitter.classList.add('dragging');
      document.body.classList.add('sidebar-dragging');
      e.preventDefault();
    });

    document.addEventListener('mousemove', function(e) {
      if (!dragging) return;
      var newWidth = startWidth + (e.clientX - startX);
      if (newWidth < MIN_PX) newWidth = MIN_PX;
      if (newWidth > MAX_PX) newWidth = MAX_PX;
      document.documentElement.style.setProperty('--sidebar-width', newWidth + 'px');
    });

    document.addEventListener('mouseup', function() {
      if (!dragging) return;
      dragging = false;
      splitter.classList.remove('dragging');
      document.body.classList.remove('sidebar-dragging');
      // 6. 存 localStorage
      var currentWidth = Math.round(sidebar.getBoundingClientRect().width);
      try {
        localStorage.setItem(STORAGE_KEY, String(currentWidth));
      } catch (err) { /* localStorage 可能被禁用, 忽略 */ }
    });

    // 7. 雙擊重置為預設 17rem (272px)
    splitter.addEventListener('dblclick', function() {
      document.documentElement.style.setProperty('--sidebar-width', '17rem');
      try { localStorage.removeItem(STORAGE_KEY); } catch (err) {}
    });
  }

  // 三層保險 (跟 lesson-home-btn 一樣)
  document.addEventListener('DOMContentLoaded', initSplitter);
  window.addEventListener('load', initSplitter);
  if (typeof MutationObserver !== 'undefined') {
    var observer = new MutationObserver(initSplitter);
    observer.observe(document.documentElement, { childList: true, subtree: true });
    setTimeout(function() { observer.disconnect(); }, 10000);
  }
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
