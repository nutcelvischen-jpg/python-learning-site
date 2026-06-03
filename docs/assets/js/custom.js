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
