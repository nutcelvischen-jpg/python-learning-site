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

/* Sidebar: 頂部 ⌂ 首頁 + ✕ 收合 雙按鈕 (JS 注入)
   mkdocs 預設 sidebar 頂部是 label.md-nav__title[for=__drawer] (logo + 站名)
   點它會 toggle drawer (桌面的常駐 sidebar 不受影響)
   我們在 logo label 下方插入一排兩個獨立按鈕:
     - ⌂ 首頁: 直接回首頁 (a 連結)
     - ✕ 收合: 點下去 toggle drawer (label[for=__drawer], 視覺上跟漢堡按鈕同步)

   注意: 桌面常駐 sidebar 時, 這兩按鈕仍顯示 (一致勝過聰明, 老大要求簡單) */
(function() {
  function addTopButtons() {
    var sidebar = document.querySelector('.md-sidebar--primary .md-nav--primary');
    if (!sidebar) return;
    if (sidebar.querySelector('.md-sidebar-top-buttons')) return;  // 避免重複

    var siteRoot = document.querySelector('a.md-header__button.md-logo').getAttribute('href') || './';

    // 包在一個 ul 裡, 跟其他 md-nav__item 同級, 視覺一致
    var container = document.createElement('li');
    container.className = 'md-nav__item md-sidebar-top-buttons';
    container.innerHTML =
      '<a href="' + siteRoot + '" class="md-nav__link md-top-btn md-top-btn--home" title="回首頁">' +
        '<span class="md-top-btn__icon" aria-hidden="true">⌂</span>' +
        '<span class="md-ellipsis">回首頁</span>' +
      '</a>' +
      '<label class="md-nav__link md-top-btn md-top-btn--close" for="__drawer" title="收合選單">' +
        '<span class="md-top-btn__icon" aria-hidden="true">✕</span>' +
        '<span class="md-ellipsis">收合</span>' +
      '</label>';

    // 插在第一個章節 li 之前 (logo label 之後)
    var firstNavItem = sidebar.querySelector('ul.md-nav__list > li');
    if (firstNavItem && firstNavItem.parentNode) {
      firstNavItem.parentNode.insertBefore(container, firstNavItem);
    } else {
      sidebar.insertBefore(container, sidebar.firstChild);
    }
  }
  document.addEventListener('DOMContentLoaded', addTopButtons);
  window.addEventListener('load', addTopButtons);
})();
