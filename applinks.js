/* 홈 화면 앱(뒤로 가기 버튼이 없는 화면)에서 갇히지 않게 해 주는 작은 도우미
   1) PDF·파일 링크는 앱 화면을 덮지 않고 '닫기' 버튼이 있는 창으로 엽니다.
   2) data-home 속성이 있는 페이지에는 ← 처음으로 버튼을 띄웁니다. */
(function () {
  var standalone = window.navigator.standalone === true ||
    (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches);

  // 1) 파일 링크
  document.addEventListener('click', function (e) {
    if (!standalone || e.defaultPrevented) return;
    var a = e.target.closest && e.target.closest('a[download], a[href$=".pdf"], a[href$=".pptx"], a[href$=".ppt"], a[href$=".hwp"], a[href$=".hwpx"]');
    if (!a || !a.getAttribute('href')) return;
    e.preventDefault();
    window.open(a.href, '_blank');
  }, true);

  // 2) 처음으로 버튼
  var me = document.currentScript;
  var home = me && me.getAttribute('data-home');
  var pos = (me && me.getAttribute('data-pos')) === 'bottom' ? 'bottom:46px' : 'top:12px';
  if (home) {
    var add = function () {
      var b = document.createElement('a');
      b.href = home;
      b.textContent = '← 처음으로';
      b.setAttribute('style', 'position:fixed;left:12px;' + pos + ';z-index:9998;background:rgba(255,255,255,.92);color:#24323a;' +
        'font:600 14px Pretendard,-apple-system,sans-serif;padding:7px 12px;border-radius:999px;text-decoration:none;' +
        'box-shadow:0 2px 10px rgba(0,0,0,.18)');
      document.body.appendChild(b);
    };
    if (document.body) add(); else document.addEventListener('DOMContentLoaded', add);
  }
})();
