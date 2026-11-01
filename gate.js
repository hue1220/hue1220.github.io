/* 화면 비밀번호 잠금 — <head> 안에 <script src="gate.js"></script> 로 넣습니다.
   비밀번호를 바꾸려면 아래 HASH 값을 새 비밀번호의 SHA-256 값으로 바꿉니다. */
(function () {
  var HASH = '164ac2402a315348ddab8fb794bcb2a0a9adcae53fb9a70ee15ae6a224acbaa6';
  var root = document.documentElement;
  root.classList.add('gate-locked');

  var css = document.createElement('style');
  css.textContent =
    'html.gate-locked body > :not(.gate){display:none !important}' +
    '.gate{position:fixed;inset:0;z-index:9999;background:#fff;display:flex;align-items:center;justify-content:center;padding:24px;' +
    "font-family:'Pretendard',-apple-system,'Apple SD Gothic Neo','Malgun Gothic',sans-serif;color:#24323a}" +
    '.gate-box{width:100%;max-width:340px;text-align:center}' +
    '.gate-box svg{width:64px;height:64px;margin-bottom:10px}' +
    '.gate-box h2{font-size:21px;font-weight:800;margin:0 0 6px}' +
    '.gate-box p{font-size:14px;color:#6b7a83;margin:0 0 20px}' +
    '.gate-box input{width:100%;box-sizing:border-box;font:inherit;font-size:24px;letter-spacing:10px;text-align:center;padding:12px;border:2px solid #e9eef0;border-radius:14px;outline:none}' +
    '.gate-box input:focus{border-color:#2EC4B6}' +
    '.gate-box input.shake{animation:gate-shake .35s;border-color:#ff6b6b}' +
    '@keyframes gate-shake{20%,60%{transform:translateX(-7px)}40%,80%{transform:translateX(7px)}}' +
    '.gate-box button{margin-top:12px;width:100%;font:inherit;font-size:16px;font-weight:700;padding:13px;border:0;border-radius:14px;background:#2EC4B6;color:#fff;cursor:pointer}' +
    '.gate-msg{min-height:20px;font-size:13px;color:#e03e3e;margin-top:10px}';
  document.head.appendChild(css);

  function sha256(text) {
    return crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)).then(function (buf) {
      return Array.from(new Uint8Array(buf)).map(function (b) { return b.toString(16).padStart(2, '0'); }).join('');
    });
  }

  function build() {
    var g = document.createElement('div');
    g.className = 'gate';
    g.innerHTML =
      '<form class="gate-box">' +
      '<svg viewBox="0 0 64 64" fill="none"><rect x="12" y="28" width="40" height="30" rx="8" fill="#e2f7f5"/>' +
      '<path d="M20 28v-7a12 12 0 0 1 24 0v7" stroke="#2EC4B6" stroke-width="4" stroke-linecap="round"/>' +
      '<circle cx="32" cy="42" r="4" fill="#2EC4B6"/><path d="M32 45v6" stroke="#2EC4B6" stroke-width="4" stroke-linecap="round"/></svg>' +
      '<h2>비밀번호를 입력하세요</h2><p>수업 시간에 알려 드린 숫자예요</p>' +
      '<input type="password" inputmode="numeric" autocomplete="off" maxlength="12" aria-label="비밀번호">' +
      '<button type="submit">들어가기</button><div class="gate-msg"></div></form>';
    document.body.appendChild(g);
    var input = g.querySelector('input'), msg = g.querySelector('.gate-msg');
    g.querySelector('form').addEventListener('submit', function (e) {
      e.preventDefault();
      var v = input.value.trim();
      if (!v) { input.focus(); return; }
      sha256(v).then(function (h) {
        if (h === HASH) { root.classList.remove('gate-locked'); g.remove(); }
        else {
          msg.textContent = '비밀번호가 맞지 않아요. 다시 입력해 보세요.';
          input.value = ''; input.classList.remove('shake'); void input.offsetWidth; input.classList.add('shake'); input.focus();
        }
      });
    });
    setTimeout(function () { input.focus(); }, 50);
  }

  if (document.body) build(); else document.addEventListener('DOMContentLoaded', build);
})();
