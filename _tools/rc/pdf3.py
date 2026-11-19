"""3일차 문제지(4쪽) · 교사용 정답표(1쪽) PDF — HTML → Playwright"""
import re, html, sys
from data3 import *
from playwright.sync_api import sync_playwright
FP = 'file:///home/claude/fonts/package'
FONTS = ''.join(f"@font-face{{font-family:P;font-weight:{w};src:url({FP}/dist/web/static/woff2/Pretendard-{n}.woff2)}}" for n,w in [('Regular',400),('Medium',500),('SemiBold',600),('Bold',700),('ExtraBold',800)])
FONTS += ''.join(f"@font-face{{font-family:SG;font-weight:{w};src:url({FP}/files/space-grotesk-latin-{w}-normal.woff2)}}" for w in (500,700))
L='ABCD'
OUT = '/home/claude/t3/out'

def plain(p):
    """해설용 지문 HTML → 문제지용: 빈칸은 (n) ____, 형광 제거"""
    p = re.sub(r'<span class="blank[^"]*" id="b(\d+)"><span class="num">\(\d+\)</span><span class="ans">[^<]*</span></span>', r'<b class="bl">(\1)</b> <span class="line"></span>', p)
    p = re.sub(r'<span class="hl" id="[^"]+">', '<span>', p)
    p = re.sub(r'<tr class="hl" id="[^"]+">', '<tr>', p)
    p = re.sub(r' id="[^"]+"', '', p)
    p = p.replace('<div class="dockind">E-MAIL</div>','').replace('<div class="dockind">NOTICE</div>','').replace('<div class="dockind">ARTICLE</div>','').replace('<div class="dockind">TEXT MESSAGES</div>','').replace('<div class="dockind">TABLE</div>','')
    return p

def opts_html(opts):
    longest = max(len(o) for o in opts)
    cls = 'g1' if longest > 30 else ('g2' if longest > 0 else '')
    return f'<div class="op {cls}">' + ''.join(f'<span><b>({L[i]})</b> {html.escape(o)}</span>' for i,o in enumerate(opts)) + '</div>'

def p5_item(it):
    n,tag,sent,opts,*_ = it
    s = html.escape(re.sub(r'\[\[(.+?)\]\]', r'\1', sent)).replace('&#x27;',"'").replace('___','<span class="line"></span>')
    return f'<div class="q"><div class="qn">{n}</div><div class="qb"><div class="st">{s}</div>{opts_html(opts)}</div></div>'

def q_item(q, stem=True):
    st = ''
    if q['part']==7:
        stm = re.sub(r'<span class="kw">(.*?)</span>', r'\1', q['stem'])
        st = f'<div class="st">{stm}</div>'
    return f'<div class="q"><div class="qn">{q["n"]}</div><div class="qb">{st}{opts_html(q["opts"])}</div></div>'

QBY = {q['n']:q for q in Q}
PB = {5:('PART 5','단문 빈칸 채우기 · 1~20번','실제 시험 30문항 (101~130번)','⏱ 10분','빈칸에 들어갈 가장 알맞은 것을 고르세요.'),
      6:('PART 6','장문 빈칸 채우기 · 21~32번','실제 시험 16문항 (131~146번)','⏱ 11분','글을 읽고 빈칸에 들어갈 가장 알맞은 단어·구·문장을 고르세요.'),
      7:('PART 7','독해 · 33~40번','실제 시험 54문항 (147~200번)','⏱ 9분','글을 읽고 질문에 가장 알맞은 답을 고르세요.')}
def pbadge(k):
    a,b,c,d,e = PB[k]
    return f'<div class="pbar"><span class="pb">{a}</span><b>{b}</b></div><div class="pbar"><span class="real">{c}</span><span class="tm">{d}</span></div><div class="ins">{e}</div>'

LOOSE = set(sys.argv[1:])
def build_problems():
    parts = []
    p5 = [p5_item(it) for it in P5]
    parts.append(f'<div class="keep">{pbadge(5)}{p5[0]}</div>')
    parts += p5[1:]
    for s in ['A','C','D','E','F','B']:
        qs = ORDER[s]
        head = pbadge(SETPART[s]) if s in ('A','E') else ''
        k = 0 if s in LOOSE else 1
        first = ''.join(q_item(QBY[n]) for n in qs[:k])
        parts.append(f'<div class="keep">{head}<div class="pi">{SETINTRO[s]}</div><div class="pass">{plain(PASS[s])}</div>{first}</div>')
        parts += [q_item(QBY[n]) for n in qs[k:]]
    body = ''.join(parts)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
@page{{size:A4;margin:13mm 12mm 12mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:P;color:#1E2433;font-size:10.2pt;line-height:1.42}}
.hd{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #3D5A80;padding-bottom:6px;margin-bottom:10px}}
.hd .k{{font:700 9pt P;color:#3D5A80;display:flex;align-items:center;gap:6px}}
.hd h1{{font:700 25pt SG,P;letter-spacing:-.01em;margin-top:2px}}.hd h1 em{{font-style:normal;color:#F2A93B}}
.hd .sub{{font-size:8.3pt;color:#6B7280}}
.hd table{{font-size:9pt;border-collapse:collapse}}.hd td{{padding:3px 4px}}.hd td.u{{border-bottom:1px solid #9AA3B2;width:72px}}
.cols{{column-count:2;column-gap:9mm;column-rule:1px solid #E3E6EC}}
.keep{{break-inside:avoid}}
.pbar{{display:flex;align-items:center;gap:7px;margin:2px 0 4px;font-size:9.2pt;white-space:nowrap}}
.pb{{background:#3D5A80;color:#fff;font:700 8.6pt SG;padding:2px 8px;border-radius:4px}}
.real{{background:#FDF1DC;color:#9a6512;font-size:7.8pt;font-weight:600;padding:1px 7px;border-radius:10px}}
.tm{{margin-left:auto;color:#3D5A80;font-weight:700;font-size:8.6pt}}
.ins{{font-size:8.6pt;color:#4B5563;margin-bottom:8px}}
.q{{display:flex;gap:7px;break-inside:avoid;margin-bottom:32px}}
.qn{{font:700 11pt SG;color:#3D5A80;min-width:18px}}
.qb{{flex:1}}.st{{margin-bottom:5px}}
.op{{display:grid;grid-template-columns:1fr 1fr;gap:2px 10px;font-size:9.8pt}}.op.g1{{grid-template-columns:1fr}}
.op b{{font:700 9pt SG;color:#3D5A80;margin-right:2px}}
.op.g1 span{{padding-left:1.9em;text-indent:-1.9em}}
.line{{display:inline-block;width:44px;border-bottom:1.2px solid #1E2433;margin:0 2px;vertical-align:-1px}}
.bl{{font:700 9.6pt SG;color:#3D5A80}}
.pi{{font-weight:700;font-size:9.3pt;margin:2px 0 5px}}
.pass{{margin-bottom:12px}}
.doc{{border:1.2px solid #C9D2DF;border-radius:8px;padding:8px 11px;font-size:9.6pt;line-height:1.36;background:#FBFCFE}}
.pass .doc+.doc,.pairdocs .doc+.doc{{margin-top:8px}}
table.mail{{border-collapse:collapse;font-size:8.8pt;margin-bottom:6px;width:100%;border-bottom:1px solid #DFE4EC}}
table.mail th{{text-align:left;width:56px;color:#5b6577;font-weight:600}}
.ptext p{{margin-bottom:5px}}.ptext p:last-child{{margin:0}}
.ttitle{{font:700 10pt SG,P;margin-bottom:4px}}.ttitle.center{{text-align:center}}
table.spec{{border-collapse:collapse;width:100%;font-size:9pt}}
table.spec th{{background:#3D5A80;color:#fff;font-weight:600;padding:2px 7px;text-align:left}}
table.spec td{{border-bottom:1px solid #DFE4EC;padding:2px 7px}}
.chatdoc{{display:flex;flex-direction:column;gap:3px;line-height:1.3}}
.chatdoc .msg{{max-width:86%}}.chatdoc .msg.r{{align-self:flex-end;text-align:right}}
.chatdoc .mh{{font-size:7.8pt;color:#5b6577}}.chatdoc .mh b{{color:#1E2433}}
.chatdoc .bub{{display:inline-block;text-align:left;background:#EEF2F8;border-radius:8px;padding:3px 8px}}
.chatdoc .msg.r .bub{{background:#FDF1DC}}
.end{{text-align:center;font:700 9pt P;color:#9AA3B2;margin-top:6px}}
</style></head><body>
<div class="hd"><div><div class="k"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#F2A93B" stroke-width="2"><circle cx="12" cy="12" r="3.2"/><circle cx="12" cy="12" r="7"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></svg>TOEIC 방과후 · RC 3일차</div>
<h1>Reading Test <em>40</em></h1><div class="sub">Part 5 · 6 · 7 | 제한 시간 30분 (Part 5 10분 · Part 6 11분 · Part 7 9분)</div></div>
<table><tr><td>반</td><td class="u"></td><td>학번</td><td class="u"></td></tr><tr><td>이름</td><td class="u"></td><td>점수</td><td class="u" style="text-align:right">/ 40</td></tr></table></div>
<div class="cols">{body}<div class="end">— 끝 —</div></div></body></html>'''

def build_key():
    KEYS = {it[0]:dict(ans=it[4],tag=it[1],star=it[9],word=it[3][L.index(it[4])]) for it in P5}
    for q in Q:
        a = q['opts'][L.index(q['ans'])]
        KEYS[q['n']] = dict(ans=q['ans'],tag=q['tag'],star=q['star'],word=a if len(a)<34 else a[:31]+'…')
    grid = ''.join(f'<div><b>{n}</b>{KEYS[n]["ans"]}</div>' for n in range(1,41))
    def rows(a,b):
        return ''.join(f'<tr><td class="n">{n}</td><td class="a">{KEYS[n]["ans"]}</td><td>{html.escape(KEYS[n]["word"])}</td><td>{KEYS[n]["tag"]}</td><td class="s">{"★"*KEYS[n]["star"]}</td></tr>' for n in range(a,b+1))
    from collections import Counter
    c = Counter(KEYS[n]['ans'] for n in KEYS); st = Counter(KEYS[n]['star'] for n in KEYS)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
@page{{size:A4;margin:12mm}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:P;color:#1E2433;font-size:8.6pt}}
h1{{font:700 17pt P;margin-bottom:2px}}h1 em{{font-style:normal;color:#F2A93B}}.sub{{color:#6B7280;font-size:8.5pt;margin-bottom:8px}}
.grid{{display:grid;grid-template-columns:repeat(10,1fr);gap:4px;margin-bottom:10px}}
.grid div{{border:1px solid #DFE4EC;border-radius:6px;text-align:center;font:700 14pt SG;color:#1F9D6B;padding:2px 0}}
.grid b{{display:block;font:500 7.5pt SG;color:#6B7280}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}
table{{border-collapse:collapse;width:100%}}th{{background:#3D5A80;color:#fff;font-weight:600;padding:3px 4px;text-align:left;font-size:8pt}}
td{{border-bottom:1px solid #E3E6EC;padding:3.2px 4px;vertical-align:top}}td.n{{font:700 9pt SG;color:#3D5A80;width:20px}}
td.a{{font:700 10pt SG;color:#1F9D6B;width:18px}}td.s{{color:#F2A93B;width:34px;white-space:nowrap}}
.foot{{margin-top:8px;font-size:8pt;color:#4B5563;line-height:1.5}}
</style></head><body><h1>RC 3일차 <em>정답표</em> (교사용)</h1>
<div class="sub">Part 5 1~20 · Part 6 21~32 · Part 7 33~40 | 정답 분포 A {c["A"]} · B {c["B"]} · C {c["C"]} · D {c["D"]} | 난이도 ★{st[1]} · ★★{st[2]} · ★★★{st[3]}</div>
<div class="grid">{grid}</div>
<div class="two"><table><tr><th>번</th><th>답</th><th>정답</th><th>유형</th><th>난도</th></tr>{rows(1,20)}</table>
<table><tr><th>번</th><th>답</th><th>정답</th><th>유형</th><th>난도</th></tr>{rows(21,40)}</table></div>
<div class="foot">2일차 복습 테스트 약점 반영: that절 + 동사원형(6·23) · 분사형용사 -ing/-ed(4·5·30) · 접속부사 흐름(24·32) · instead of/rather than(18) · 동사 뒤 부사(2) · 전치사 vs 접속사(16·17·26) · meet a deadline(10) · 쉬운 단어의 다른 뜻(25·33 free, 37 directed)</div>
</body></html>'''

def render(h, out):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        open(out.replace('.pdf','.html'),'w').write(h)
        pg.goto('file://'+out.replace('.pdf','.html')); pg.wait_for_timeout(600)
        pg.pdf(path=out, format='A4', print_background=True, prefer_css_page_size=True)

if __name__=='__main__':
    import os; os.makedirs(OUT, exist_ok=True)
    render(build_problems(), OUT+'/problems.pdf')
    render(build_key(), OUT+'/key.pdf')
    print('done')
