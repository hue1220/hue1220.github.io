"""3일차 복습 노트(2쪽) PDF + 복습 테스트(웹 채점) 데이터·페이지"""
import random, json, re, sys
from collections import Counter
from pdf3 import FONTS, render, OUT

# ---- 꿀팁 12: (번호, 제목, 문항, 설명, [예문(<g>강조</g>)]) ----
TIPS = [
('01','품사 자리 — 앞뒤 두 단어로','1, 2, 3, 30','a + (형용사) + ___ + of → 명사 / be (more) ___ → 형용사 / 동사(+목적어) 뒤 → <b>-ly 부사</b>',
 ['He gave a detailed <g>explanation</g> of the plan.','Please operate the machine <g>safely</g>.']),
('02','감정 분사 — 사물 -ing · 사람 -ed','4, 5, 30','<b>주어부터</b> 보기: 사물이 감정을 주면 -ing, 사람이 느끼면 -ed. 사물이 "~된" 상태도 -ed',
 ['The results were <g>disappointing</g>.','Many students were <g>interested</g> in the class.']),
('03','that절 + 동사원형','6, 23','require · important · necessary + that + 주어 + <b>동사원형</b> (주어가 단수여도 -s ✕)',
 ['It is important that every worker <g>complete</g> the course.','He requires that she <g>wear</g> gloves.']),
('04','시제 단서 찾기','7, 21, 29','since + 시점 → have p.p. / next ~ → will / 원래 → 바뀐 상태 → has been p.p.',
 ['Mr. Park <g>has worked</g> here since 2019.','The factory <g>will open</g> next spring.']),
('05','수동태 — 뒤에 목적어가 없으면','8, 21','주어가 "당하는" 쪽 + 빈칸 뒤 목적어 없음 / by ~ → <b>be p.p.</b>',
 ['The belt <g>will be installed</g> next Monday.','The training <g>has been moved</g> to Dec 2.']),
('06','수일치 — 전치사 덩어리는 괄호','9','주어 (for/of ~) 동사 → 괄호 밖 <b>진짜 주어</b>에 맞추기',
 ['The instructions (for the machine) <g>are</g> here.','The list (of names) <g>is</g> on the desk.']),
('07','어휘 짝꿍 — 덩어리로 외우기','10, 14, 25, 28','빈칸 + 짝 명사를 소리 내 읽어 보기',
 ['<g>meet</g> a deadline · <g>offer</g> a refund','<g>free</g> shuttle bus · We <g>appreciate</g> your cooperation.']),
('08','숫자 앞 부사 · 비교급 강조','12, 20','숫자 앞 → nearly · approximately / 비교급 앞 → <b>much · far · even</b> (very ✕)',
 ['They hired <g>nearly</g> 30 workers.','Sales were <g>far</g> higher than last year.']),
('09','전치사 vs 접속사 — 빈칸 뒤 먼저','16, 17, 18, 26','명사만 → 전치사(despite · during · instead of) / 주어+동사 → 접속사(although · while)',
 ['<g>Despite</g> the rain, we played. / <g>Even though</g> it rained, …','Be quiet <g>while</g> you are here. · repair it <g>instead of</g> buying one']),
('10','재귀대명사 — by oneself','19','by + -self = 혼자서, 스스로 (by them = 그들에 의해 ✕)',
 ['Ms. Kim and her team did it by <g>themselves</g>.','I fixed my bike by <g>myself</g>.']),
('11','Part 6 문장 삽입 · 흐름','22, 24, 27, 31, 32','보기 속 She · there · However가 앞 문장과 이어지는지 / 앞뒤 관계: 반대 However · 결과 Therefore · 추가 In addition',
 ['All must attend. <g>However</g>, only 15 seats are left.','We will hire 200 people. <g>In addition</g>, we will train them.']),
('12','Part 7 — 쉬운 단어의 다른 뜻 · 바꿔 말하기','33~40','free = 무료 / <b>비어 있는</b> · directed to = <b>sent to</b> · robots → equipment',
 ['The printer upstairs is <g>free</g> (= available) now.','Questions can be <g>directed</g> (= sent) to Ms. Park.']),
]
WORDS = [('explanation','설명'),('operate','작동하다, 운전하다'),('attractive','매력적인'),('disappointing','실망스러운'),('be interested in','~에 관심이 있다'),
('require','요구하다'),('protective gloves','보호 장갑'),('install','설치하다'),('instructions','설명서, 지시'),('meet a deadline','마감을 지키다'),
('identification card','신분증'),('nearly','거의'),('authorized','권한을 받은'),('refund','환불'),('currently','현재'),
('out of order','고장 난'),('despite','~에도 불구하고'),('even though','~인데도'),('instead of','~ 대신에'),('by oneself','혼자서, 스스로'),
('originally','원래'),('scheduling conflict','일정이 겹침'),('free','무료의 / 비어 있는'),('appreciate','감사하다'),('automated','자동화된'),
('skilled','숙련된'),('in addition','게다가'),('opening hours','운영 시간'),('free of charge','무료로'),('equipment','장비')]
CHECK = [('The results were ( disappointing / disappointed ) to us.','disappointing'),('She is ( interested / interesting ) in robots.','interested'),
('It is important that he ( arrive / arrives ) on time.','arrive'),('Please drive ( safe / safely ).','safely'),
('( Despite / Although ) the snow, we went out.','Despite'),('Stay quiet ( during / while ) the test is going on.','while'),
('I walked ( instead of / rather ) taking a bus.','instead of'),('The list of names ( is / are ) on the desk.','is'),
('We need to ( meet / attend ) the deadline.','meet'),('Sales were ( very / far ) better this year.','far')]

def note_html():
    def ex(e): return re.sub(r'<g>(.*?)</g>', r'<em>\1</em>', e)
    tips = ''.join(f'<div class="tip"><div class="th"><span class="tn">{n}</span><b>{t}</b><span class="nums">{q}</span></div><p>{d}</p>' + ''.join(f'<div class="ex">{ex(e)}</div>' for e in es) + '</div>' for n,t,q,d,es in TIPS)
    words = ''.join(f'<tr><td class="wn">{i}</td><td class="we">{w}</td><td>{k}</td><td class="ck">○</td></tr>' for i,(w,k) in enumerate(WORDS[:15],1))
    words2 = ''.join(f'<tr><td class="wn">{i}</td><td class="we">{w}</td><td>{k}</td><td class="ck">○</td></tr>' for i,(w,k) in enumerate(WORDS[15:],16))
    chk = ''.join(f'<div><b>{i}.</b> {q}</div>' for i,(q,a) in enumerate(CHECK,1))
    ans = '정답 — ' + ' · '.join(f'{i}. {a}' for i,(q,a) in enumerate(CHECK,1))
    lines = ''.join('<tr><td></td><td></td><td></td></tr>' for _ in range(10))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
@page{{size:A4;margin:11mm 12mm}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:P;color:#1E2433;font-size:8.6pt;line-height:1.4}}
.page{{height:275mm;overflow:hidden;page-break-after:always}}.page:last-child{{page-break-after:auto}}
.hd{{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #3D5A80;padding-bottom:5px;margin-bottom:7px}}
.hd h1{{font:800 17pt P}}.hd h1 em{{font-style:normal;color:#F2A93B}}.hd .s{{font-size:8pt;color:#6B7280}}
.idb{{display:flex;gap:6px}}.idb span{{border:1px solid #C9D2DF;border-radius:6px;padding:4px 8px;width:92px;color:#9AA3B2;font-size:8pt}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:10px}}
.steps div{{background:#EEF2F8;border-radius:8px;padding:5px 8px;font-size:7.8pt}}.steps b{{display:block;color:#3D5A80;font-size:8.4pt}}
.steps div:last-child{{background:#FDF1DC}}.steps div:last-child b{{color:#9a6512}}
.sec{{display:flex;align-items:center;gap:7px;margin:3px 0 6px;font-weight:700;font-size:10pt}}.sec span{{background:#3D5A80;color:#fff;font-size:8pt;padding:2px 8px;border-radius:4px}}.sec small{{font-weight:400;color:#6B7280;font-size:7.8pt}}
.tips{{display:grid;grid-template-columns:1fr 1fr;gap:9px}}
.tip{{border:1px solid #DFE4EC;border-radius:8px;padding:8px 10px}}
.th{{display:flex;align-items:center;gap:6px;margin-bottom:2px}}.tn{{background:#3D5A80;color:#fff;font:700 8pt SG;border-radius:4px;padding:1px 5px}}
.th b{{font-size:9.8pt}}.nums{{margin-left:auto;color:#9AA3B2;font-size:7.4pt}}
.tip p{{font-size:8.7pt;color:#374151;margin-bottom:4px;line-height:1.45}}
.ex{{background:#F3F8F5;border-radius:5px;padding:3px 8px;margin-top:3px;font-size:9pt}}.ex em{{font-style:normal;font-weight:700;color:#1F9D6B}}
table.w{{border-collapse:collapse;width:100%;font-size:9.4pt}}table.w td{{border-bottom:1px solid #E3E6EC;padding:5.4px 4px}}
.wn{{color:#9AA3B2;width:18px}}.we{{font-weight:700;width:42%}}.ck{{color:#9AA3B2;width:16px;text-align:right}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.chk{{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;font-size:9.6pt;margin-bottom:7px}}.chk b{{color:#3D5A80}}
.ans{{transform:rotate(180deg);font-size:7.4pt;color:#9AA3B2;text-align:center;margin-bottom:10px}}
table.o{{border-collapse:collapse;width:100%}}table.o th{{background:#EEF2F8;font-size:8pt;padding:3px;text-align:left}}table.o td{{border-bottom:1px solid #DFE4EC;height:30px}}
</style></head><body>
<div class="page"><div class="hd"><div><h1>복습 노트 · <em>꿀팁 12 + 단어 30</em></h1><div class="s">방과후 기초영어반 · 3일차 · 자습 30분</div></div><div class="idb"><span>학번</span><span>이름</span></div></div>
<div class="steps"><div><b>① 꿀팁 12개 읽기</b>초록 예문을 소리 내 한 번씩</div><div><b>② 단어 30개 외우기</b>뜻을 가리고 말해 보고 ○ 체크</div><div><b>③ 확인 문제 10개</b>답은 맨 아래 거꾸로</div><div><b>④ 복습 테스트</b>40문항 중 32개(80%) 이상 통과, 자료실에서 응시</div></div>
<div class="sec"><span>꿀팁</span>오늘 나온 유형 공략 12 <small>오른쪽 숫자 = 오늘 문제 번호</small></div><div class="tips">{tips}</div></div>
<div class="page"><div class="sec"><span>단어</span>핵심 단어 30 <small>외웠으면 ○에 체크</small></div>
<div class="two"><table class="w">{words}</table><table class="w">{words2}</table></div>
<div class="sec" style="margin-top:12px"><span>확인</span>괄호 안에서 알맞은 말에 동그라미 하세요.</div><div class="chk">{chk}</div><div class="ans">{ans}</div>
<div class="sec"><span>오답</span>3일차에 틀린 문제 정리 <small>틀린 번호 → 위 꿀팁 번호 찾기 → 다음엔 이렇게!</small></div>
<table class="o"><tr><th style="width:18%">틀린 번호</th><th style="width:18%">꿀팁 번호</th><th>다음엔 이렇게 풀기 (한 줄)</th></tr>{lines}</table></div>
</body></html>'''

# ---- 복습 테스트 40 (첫 보기가 정답, 아래에서 섞음) ----
QZ = [
("He gave a clear ______ of the rules.",['explanation','explain','explanatory','explained'],'꿀팁 01','품사 자리'),
("Please handle the boxes ______.",['carefully','careful','care','carefulness'],'꿀팁 01','품사 자리'),
("This new phone is very ______.",['attractive','attract','attraction','attractively'],'꿀팁 01','품사 자리'),
("The game was really ______.",['boring','bored','bore','boredom'],'꿀팁 02','분사형용사'),
("I was ______ by the news.",['surprised','surprising','surprise','surprisingly'],'꿀팁 02','분사형용사'),
("It is necessary that he ______ the report today.",['send','sends','sending','to send'],'꿀팁 03','that절 + 원형'),
("Ms. Lee ______ here since 2020.",['has worked','works','worked','will work'],'꿀팁 04','시제'),
("The new machine ______ tomorrow.",['will be installed','installs','will install','installing'],'꿀팁 05','수동태'),
("The keys to the office ______ on the desk.",['are','is','being','has'],'꿀팁 06','수일치'),
("We must ______ the deadline.",['meet','attend','join','fill'],'꿀팁 07','어휘 짝꿍'),
("The store will ______ a full refund.",['offer','spend','ask','take'],'꿀팁 07','어휘 짝꿍'),
("______ 100 people came to the show.",['Nearly','Lately','Hardly','Closely'],'꿀팁 08','숫자 앞 부사'),
("______ the rain, we played soccer.",['Despite','Although','Because','Unless'],'꿀팁 09','전치사 vs 접속사'),
("______ it was cold, he went swimming.",['Even though','Despite','Because of','In spite of'],'꿀팁 09','전치사 vs 접속사'),
("I took the bus ______ walking.",['instead of','rather','so that','in order to'],'꿀팁 09','instead of vs rather than'),
("I fixed my bike by ______.",['myself','me','my','mine'],'꿀팁 10','재귀대명사'),
("'authorized'의 뜻은?",['권한을 받은','자동의','매년의','정확한'],'단어','단어'),
("'out of order'의 뜻은?",['고장 난','주문한','정리된','순서대로'],'단어','단어'),
("'currently'의 뜻은?",['현재','이전에','마침내','거의'],'단어','단어'),
("\"The room is free now.\"에서 free의 뜻은?",['비어 있는(사용 가능한)','무료인','쉬운','닫힌'],'꿀팁 12','단어(다의어)'),
("Workers must ______ follow the safety rules.",['strictly','strict','strictness','stricter'],'꿀팁 01','품사 자리'),
("The movie was ______, so we left early.",['disappointing','disappointed','disappoint','disappointment'],'꿀팁 02','분사형용사'),
("The students were ______ in the science class.",['interested','interesting','interest','interestingly'],'꿀팁 02','분사형용사'),
("The manager requires that each worker ______ a helmet.",['wear','wears','wearing','to wear'],'꿀팁 03','that절 + 원형'),
("(Date: November 18) The new gym ______ next month.",['will open','opened','has opened','was opening'],'꿀팁 04','시제'),
("The windows ______ every week by the staff.",['are cleaned','clean','cleaning','are cleaning'],'꿀팁 05','수동태'),
("The boxes in the truck ______ heavy.",['are','is','being','has'],'꿀팁 06','수일치'),
("We ______ your help.",['appreciate','apologize','deserve','expect'],'꿀팁 07','어휘 짝꿍'),
("This car is ______ faster than mine.",['far','very','many','most'],'꿀팁 08','비교급 강조'),
("Please be quiet ______ you are in the library.",['while','during','despite','because of'],'꿀팁 09','전치사 vs 접속사'),
("The game was canceled ______ the heavy snow.",['because of','because','although','while'],'꿀팁 09','전치사 vs 접속사'),
("The children cleaned the room by ______.",['themselves','them','their','they'],'꿀팁 10','재귀대명사'),
("The bus is late. ______, we will take a taxi.",['Therefore','For example','Similarly','However'],'꿀팁 11','흐름(접속부사)'),
("She is a good cook. ______, she bakes great bread.",['In addition','However','Instead','Otherwise'],'꿀팁 11','흐름(접속부사)'),
("The test was hard. ______, everyone passed.",['However','Therefore','In addition','For example'],'꿀팁 11','흐름(접속부사)'),
("Mina lost her phone. [ ? ] She finally found it under her bed. — [ ? ]에 들어갈 문장은?",['She looked for it everywhere.','She bought a new laptop.','Her brother likes soccer.','The weather was nice.'],'꿀팁 11','문장 삽입'),
("\"Questions can be directed to Mr. Kim.\"에서 directed와 같은 뜻은?",['sent','ordered','managed','pointed'],'꿀팁 12','바꿔 말하기'),
("\"All courses are free.\"와 같은 뜻은?",['The courses are free of charge.','The courses are online.','The courses are long.','The courses are full.'],'꿀팁 12','바꿔 말하기'),
("'equipment'의 뜻은?",['장비','직원','설명서','신분증'],'단어','단어'),
("'appreciate'의 뜻은?",['감사하다','사과하다','기대하다','설치하다'],'단어','단어'),
]

def quiz_items(seed=319):
    rnd = random.Random(seed)
    while True:
        seq = [rnd.choice('ABCD') for _ in QZ]
        c = Counter(seq)
        if all(c[x]==10 for x in 'ABCD') and not any(seq[i]==seq[i+1]==seq[i+2] for i in range(len(seq)-2)): break
    out = []
    for (q,opts,t,ty),a in zip(QZ,seq):
        cor = opts[0]; d = opts[1:]; rnd.shuffle(d); i='ABCD'.index(a)
        o = d[:i]+[cor]+d[i:]
        out.append(dict(q=q,o=o,a=i,t=t,type=ty))
    return out

def quiz_page(items):
    tpl = open('/home/claude/hue1220.github.io/t2/quiz/index.html').read()
    tpl = tpl.replace('기초영어반 2일차 복습 테스트','기초영어반 3일차 복습 테스트').replace('<h1>2일차 복습 테스트</h1>','<h1>3일차 복습 테스트</h1>')
    js = json.dumps([dict(q=x['q'],o=x['o'],a=x['a'],t=x['t']) for x in items], ensure_ascii=False)
    tpl = re.sub(r'const Q=\[.*?\];const L=', 'const Q='+js.replace('\\','\\\\')+';const L=', tpl, count=1, flags=re.S)
    tpl = tpl.replace("const LESSON='2차시'","const LESSON='3차시'")
    assert "LESSON='3차시'" in tpl and '3일차 복습 테스트' in tpl and 'ENDPOINT=' in tpl and '/^\\d{4}$/' in tpl
    return tpl

if __name__=='__main__':
    import os; os.makedirs(OUT, exist_ok=True)
    render(note_html(), OUT+'/review.pdf')
    items = quiz_items()
    os.makedirs(OUT+'/quiz', exist_ok=True)
    open(OUT+'/quiz/index.html','w').write(quiz_page(items))
    json.dump(items, open(OUT+'/quiz_items.json','w'), ensure_ascii=False, indent=1)
    print(''.join('ABCD'[x['a']] for x in items))
