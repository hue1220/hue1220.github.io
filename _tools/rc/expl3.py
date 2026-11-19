"""기초영어반 3일차 RC 해설 화면 — 단일 HTML (2일차 생성기 구조 그대로, 데이터만 data3)."""
import os, re, json, base64, subprocess, html, sys
from data3 import *
D = os.path.dirname(os.path.abspath(__file__))
FP = '/home/claude/fonts/package'
PR = FP + '/dist/web/static/woff2/Pretendard-%s.woff2'
SG = FP + '/files/space-grotesk-latin-%s-normal.woff2'
DAY = '3일차'
CSS = open(D+'/css.txt').read()
JS = open(D+'/js.txt').read()
L = 'ABCD'
QBY = {q['n']:q for q in Q}

def badge(part):
    return {6:'<span class="pb">PART 6</span><span class="real">실제 시험 16문항 (131~146번)</span>',
            7:'<span class="pb">PART 7</span><span class="real">실제 시험 54문항 (147~200번)</span>'}[part]
GEAR = '<svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#F2A93B" stroke-width="1.5"><circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/><circle cx="12" cy="12" r="6.5"/></svg>'

slides = []
slides.append((f'''<div class="cover">{GEAR}<div class="ck">TOEIC 방과후 · RC {DAY} 해설</div><h1>Reading Test <em>40</em><br>해설</h1>
<p>Part 5 &nbsp;1~20번 &nbsp;·&nbsp; Part 6 &nbsp;21~32번 &nbsp;·&nbsp; Part 7 &nbsp;33~40번</p><div class="hint">화면을 터치하거나 Enter를 누르면 한 단계씩 진행돼요</div></div>''', 0, '표지'))

def setcls(s): return {'B':'wide','E':'chat'}.get(s,'')
def read_slide(s):
    return (f'''<div class="topbar">{badge(SETPART[s])}<span class="ttl">{SETTITLE[s]}</span><span class="step">지문 먼저 읽기</span></div>
<div class="readwrap {setcls(s)}"><div class="readp">{PASS[s]}</div><div class="readguide">{GUIDE[s]}</div></div>''', 0, SETTITLE[s].split(' ·')[0]+' 지문')

def q_slide(q):
    sid = f"q{q['n']}"
    passage = re.sub(r'id="([^"]+)"', lambda m: f'id="{sid}-{m.group(1)}"', PASS[q['set']])
    if q['cur']:
        for c in ('blank long','blank '):
            passage = passage.replace(f'class="{c}" id="{sid}-{q["cur"]}"', f'class="{c.strip()} cur" id="{sid}-{q["cur"]}" data-fillon="{q["fill"]}"')
    hlspec = {f'{sid}-{h[0]}':(h[1],h[2],h[3] if len(h)>3 else '') for h in q['hl']}
    found = set()
    def addhl(m):
        i = m.group(1)
        if i in hlspec:
            found.add(i); s,k,mk = hlspec[i]
            return f'id="{i}" data-hl="{s}" data-kind="{k}"' + (f' data-mark="{mk}"' if mk else '')
        return m.group(0)
    passage = re.sub(r'id="([^"]+)"', addhl, passage)
    miss = set(hlspec) - found
    assert not miss, (q['n'], miss)
    focus = ''
    if q['focus']:
        for f in q['focus']:
            assert f'class="sen" id="{sid}-{f}"' in passage, (q['n'], f)
            passage = passage.replace(f'class="sen" id="{sid}-{f}"', f'class="sen focus" id="{sid}-{f}"')
        focus = 'data-dimon="2"'
    ol = ''.join(f'<li class="opt {"ok" if L[i]==q["ans"] else "no"}"><b>({L[i]})</b> {html.escape(o)}</li>' for i,o in enumerate(q['opts']))
    ex = ''.join(f'<div class="ex" data-on="{s}">{t}</div>' for s,t in q['expl'])
    last = max(s for s,_ in q['expl']) + 1
    right = f'''<div class="qcard"><div class="qhead"><span class="qn">{q["n"]}</span><span class="tag" data-on="1">{q["tag"]}</span></div>
<div class="stem">{q["stem"]}</div><ol class="opts">{ol}</ol>{ex}
<div class="tip" data-on="{last}"><span>💡 꿀팁</span>{q["tip"]}</div><div class="memo" data-on="{last}"><span>외워 두기</span>{q["memo"]}</div></div>'''
    h = f'''<div class="topbar">{badge(q["part"])}<span class="ttl">{SETTITLE[q["set"]]}</span><span class="step">{q["n"]}번</span></div>
<div class="split {setcls(q["set"])}"><div class="left" {focus}>{passage}</div><div class="right">{right}</div></div>'''
    return (h, last, f'{q["n"]}번')

def done_slide(s):
    d = re.sub(r'id="([^"]+)"', lambda m: f'id="c{s}-{m.group(1)}"', PASS[s]).replace('class="blank ', 'class="blank filled ').replace('class="blank long', 'class="blank filled long')
    li = ''.join(f'<li>({n}) <b>{a}</b> — {w}</li>' for n,a,w in DONE[s])
    return (f'''<div class="topbar">{badge(6)}<span class="ttl">{SETTITLE[s]}</span><span class="step">완성 지문</span></div>
<div class="readwrap"><div class="readp">{d}</div><div class="readguide"><h3>정답 채워 다시 읽기</h3><ol>{li}</ol><div class="tipbox">초록 글자를 넣고 소리 내 한 번 읽어 보기</div></div></div>''', 0, SETTITLE[s].split(' ·')[0]+' 완성')

P5_INTRO = f'''<div class="topbar"><span class="pb">PART 5</span><span class="real">실제 시험 30문항 (101~130번)</span><span class="ttl">1–20번 · 단문 빈칸</span><span class="step">유형 공략</span></div>
<div class="intro5"><h2>Part 5, 이렇게 풀어요</h2>
<div class="i5grid"><div class="i5"><b>1</b><h3>보기 4개부터</h3><p>같은 단어의 변형? <em>→ 자리 문제</em><br>뜻이 다른 단어들? <em>→ 어휘 문제</em></p></div>
<div class="i5"><b>2</b><h3>자리 문제</h3><p>해석 말고 <em>빈칸 앞뒤 두 단어</em>만 보고 품사 결정 — 10초</p></div>
<div class="i5"><b>3</b><h3>어휘 문제</h3><p>빈칸과 <em>짝이 되는 단어</em>(목적어·명사)부터 — 30초</p></div></div>
<div class="tipbox big">⏱ 실제 시험: 30문항 15분 · 오늘 20문항 10분 — 모르는 문제는 찍고 넘어가기!</div></div>'''

def p5_slide(item):
    n,tag,sent,opts,ans,expl,wrong,tip,memo,star = item
    sid=f'p{n}'; k=[0]
    def hl(m):
        k[0]+=1; return f'<span class="hl" id="{sid}-h{k[0]}" data-hl="2" data-kind="y" data-mark="{k[0]}">{m.group(1)}</span>'
    s = re.sub(r'\[\[(.+?)\]\]', hl, html.escape(sent).replace('&#x27;',"'"))
    s = s.replace('___', f'<span class="blank cur" id="{sid}-b" data-fillon="1"><span class="num"></span><span class="ans">{opts[L.index(ans)]}</span></span>')
    ol = ''.join(f'<li class="opt {"ok" if L[i]==ans else "no"}"><b>({L[i]})</b> {html.escape(o)}</li>' for i,o in enumerate(opts))
    ex = ''.join(f'<div class="ex" data-on="2">{t}</div>' for t in expl) + f'<div class="ex" data-on="3">{wrong}</div>'
    h = f'''<div class="topbar"><span class="pb">PART 5</span><span class="real">실제 시험 30문항 (101~130번)</span><span class="ttl">1–20번 · 단문 빈칸</span><span class="step">{n}번</span></div>
<div class="p5wrap qcard"><div class="qhead"><span class="qn">{n}</span><span class="tag" data-on="1">{tag}</span></div>
<div class="p5sent">{s}</div><ol class="opts p5opts">{ol}</ol>
<div class="p5ex">{ex}</div>
<div class="p5foot"><div class="tip" data-on="4"><span>💡 꿀팁</span>{tip}</div><div class="memo" data-on="4"><span>외워 두기</span>{memo}</div></div></div>'''
    return (h, 4, f'{n}번')

slides.append((P5_INTRO, 0, 'Part 5 공략'))
for it in P5: slides.append(p5_slide(it))
for s in ['A','C','D','E','F','B']:
    slides.append(read_slide(s))
    for n in ORDER[s]: slides.append(q_slide(QBY[n]))
    if s in DONE: slides.append(done_slide(s))
KEY = {q['n']:q['ans'] for q in Q}; KEY.update({it[0]:it[4] for it in P5})
ansgrid = ''.join(f'<div><b>{n}</b>{KEY[n]}</div>' for n in range(1,41))
slides.append((f'''<div class="cover end">{GEAR}<div class="ck">정답 한눈에 · 1~40번</div><div class="agrid">{ansgrid}</div>
<div class="next"><b>다음 활동</b> — 오늘 틀린 문항의 <u>근거 문장</u>에 밑줄 긋고, 💡꿀팁 한 줄을 복습 노트에 옮겨 적기 → 자료실에서 <b>복습 테스트</b>(40문항, 32개 이상 통과)</div></div>''', 0, '정답 한눈에'))

colors = ['E0A100','3D5A80','1F9D6B','D9534F']
markers = ''.join(f'<marker id="m{c}" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#{c}"/></marker>' for c in colors)
body = ''.join(f'<section class="slide" data-steps="{st}" data-links=\'[]\'>{h}<svg class="links"><defs>{markers}</defs></svg></section>' for h,st,lab in slides)
listbtn = ''.join(f'<button data-i="{i}">{lab}</button>' for i,(h,st,lab) in enumerate(slides))

text = re.sub(r'<[^>]+>', ' ', body + listbtn) + CSS + '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz/ –—·()$%.,:;!?\'"~↓↔⇄→←①②③④⑤⏱💡✓✕ 정답한눈에다음활동이전목록전체화면◀ '
text = html.unescape(text)
open(D+'/chars.txt','w').write(''.join(sorted(set(text))))
fontcss = ''
for name,w in [('Regular',400),('SemiBold',600),('Bold',700),('ExtraBold',800)]:
    out = f'{D}/sub-{w}.woff2'
    subprocess.run(['pyftsubset', PR%name, f'--text-file={D}/chars.txt', '--flavor=woff2', f'--output-file={out}', '--layout-features=*'], check=True)
    fontcss += f"@font-face{{font-family:Pretendard;font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(out,'rb').read()).decode()})}}"
for w in (500,700):
    fontcss += f"@font-face{{font-family:'Space Grotesk';font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(SG%w,'rb').read()).decode()})}}"

doc = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>RC {DAY} 해설</title>
<style>{fontcss}{CSS}</style></head><body><div id="stage">{body}</div>
<div id="nav"><button id="bp">◀ 이전</button><button id="bl">목록</button><button id="bf">전체화면</button></div><div id="pg"></div>
<div id="list"><div>{listbtn}</div></div><script>{JS}</script><script src="../applinks.js?v=1" data-home="../english/" data-pos="bottom"></script></body></html>'''
out = sys.argv[1] if len(sys.argv)>1 else D+'/RC_3일차_해설.html'
open(out,'w').write(doc)
print('slides', len(slides), 'size KB', len(doc)//1024)
