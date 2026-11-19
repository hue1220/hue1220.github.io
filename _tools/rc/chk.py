import sys
from playwright.sync_api import sync_playwright
f=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file://'+f); pg.wait_for_timeout(800)
    n=pg.evaluate('__kai.n()')
    bad=pg.evaluate('''(n)=>{const out=[];for(let i=0;i<n;i++){const s=__kai.S[i];const st=+s.dataset.steps;__kai.go(i,st);
      const sr=document.getElementById('stage').getBoundingClientRect();let mb=0,mr=0;
      s.querySelectorAll('*').forEach(e=>{if(e.closest('svg'))return;const r=e.getBoundingClientRect();if(r.width==0||r.height==0)return;
        const cs=getComputedStyle(e);if(cs.display=='none'||cs.visibility=='hidden')return;mb=Math.max(mb,r.bottom-sr.top);mr=Math.max(mr,r.right-sr.left);});
      ['.right','.left','.p5wrap','.readp','.qcard'].forEach(q=>{const e=s.querySelector(q);if(e&&e.scrollHeight>e.clientHeight+2)out.push([i,q,'scroll',e.scrollHeight,e.clientHeight]);});
      if(mb>1075||mr>1915)out.push([i,'bounds',Math.round(mb),Math.round(mr)]);}return out;}''',n)
    print(n,'slides'); [print(x) for x in bad]
    for i in map(int,sys.argv[2:]):
        st=pg.evaluate(f'__kai.S[{i}].dataset.steps'); pg.evaluate(f'__kai.go({i},{st})'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'/home/claude/t3/s{i}.png')
