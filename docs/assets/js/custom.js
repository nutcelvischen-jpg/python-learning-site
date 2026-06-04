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

/* Sidebar: 永遠展開所有章節, 不能收合
   mkdocs material 用 <input type=checkbox> + :checked 配 <nav> 顯示
   我們在 load 時把所有 sidebar 的 checkbox 都打勾,
   並把章節 input 設為 disabled (讓它不能被點擊 toggle) */
(function() {
  function expandAllSidebarSections() {
    var primary = document.querySelector('.md-sidebar--primary');
    if (!primary) return;
    // 把所有章節的 checkbox 都設為 checked + disabled
    var checkboxes = primary.querySelectorAll('input[type="checkbox"].md-nav__toggle');
    checkboxes.forEach(function(cb) {
      cb.checked = true;
      cb.disabled = true;  // 不能 toggle
    });
  }
  // DOMContentLoaded + load 雙保險
  document.addEventListener('DOMContentLoaded', expandAllSidebarSections);
  window.addEventListener('load', expandAllSidebarSections);
})();
