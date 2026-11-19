"""기초영어반 3일차 RC 40문항 — 해설·문제지·정답표 공통 데이터 (2026-11-19)"""

def B(n, ans, cls=''):
    return f'<span class="blank {cls}" id="b{n}"><span class="num">({n})</span><span class="ans">{ans}</span></span>'
def H(i, t):
    return f'<span class="hl" id="{i}">{t}</span>'
C = lambda n, k='': f'<i class="c {k}">{n}</i>'

# ---------------- Part 5 ----------------
# (n, tag, sentence, opts, ans, expl, wrong, tip, memo, star)
P5 = [
(1,'명사 자리','The factory manager asked for [[a detailed]] ___ [[of]] the repair costs.',['explanatory','explanation','explain','explained'],'B',
 [f'{C(1)} a + 형용사(detailed) + <b>빈칸</b> + {C(2)} of → 빈칸은 <b>명사</b> 자리'],
 '오답: explanatory(형용사) · explain(동사) · explained(p.p.) — detailed가 이미 형용사라 형용사가 또 올 수 없어요.',
 'a + (형용사) + ___ + of → <b>명사</b>. 꼬리 -tion · -ment · -ance는 명사!','a detailed explanation of ~ = ~에 대한 자세한 설명',2),
(2,'부사 자리 (동사 뒤)','Forklift drivers must [[operate the vehicles]] ___ inside the warehouse.',['safer','safety','safe','safely'],'D',
 [f'{C(1)} 동사 + 목적어(operate the vehicles) 뒤 → 동사를 꾸미는 <b>부사</b>'],
 '함정 safe(형용사): 1·2일차에 careful을 고른 함정과 똑같아요! safety(명사) · safer(형용사 비교급)',
 '동사(+목적어) 뒤 빈칸 = <b>-ly 부사</b> (drive carefully · operate safely)','operate safely = 안전하게 운전하다',2),
(3,'형용사 자리','The new packaging design [[is much more]] ___ [[than]] the old one.',['attractive','attract','attraction','attractively'],'A',
 [f'{C(1)} be + more + 빈칸 + {C(2)} than → 비교급 보어 자리 = <b>형용사</b>'],
 '오답: attract(동사) · attraction(명사) · attractively(부사 — be 뒤 보어 자리에 못 와요)',
 'be (more) ___ (than) → <b>형용사</b>. 꼬리 -ive · -ful · -able','attractive = 매력적인',2),
(4,'분사형용사 (사물 -ing)','[[The results]] of the customer survey were ___ to the sales team.',['disappointed','disappointment','disappoint','disappointing'],'D',
 [f'{C(1)} 주어 = 결과(<b>사물</b>) → 실망을 <b>주는</b> 쪽 = <b>-ing</b>'],
 '함정 disappointed: 사람(sales team)이 느끼는 감정이에요. 주어는 results! disappointment(명사) · disappoint(동사)',
 '<b>사물이 감정을 주면 -ing</b>, 사람이 감정을 느끼면 -ed — 주어부터 확인','disappointing results = 실망스러운 결과',2),
(5,'분사형용사 (사람 -ed)','[[Many participants]] were ___ [[in]] the new welding course.',['interestingly','interest','interested','interesting'],'C',
 [f'{C(1)} 주어 = <b>사람</b> → 관심을 <b>느낌</b> = <b>-ed</b>', f'{C(2)} be interested in ~ = ~에 관심이 있다'],
 '함정 interesting: 관심을 <b>주는</b> 것(과정이 interesting). interest(명사·동사) · interestingly(부사)',
 '<b>사람이 느끼면 -ed</b>, 감정을 주는 것이면 -ing','be interested in ~ = ~에 관심이 있다',2),
(6,'that절 + 동사원형','The safety manager [[requires that]] [[each employee]] ___ protective gloves in the workshop.',['wear','to wear','wearing','wears'],'A',
 [f'{C(1)} require that + 주어 + <b>동사원형</b>', f'{C(2)} 주어가 each employee(단수)여도 <b>-s를 붙이지 않아요</b>'],
 '함정 wears: 단수 주어에 끌림 — 2일차 34번 submits와 같은 함정! wearing · to wear는 동사 자리에 못 와요.',
 '요구·중요·필요(require · important · necessary) + <b>that</b> → 주어가 she여도 <b>동사원형</b>','require that + 주어 + 동사원형',3),
(7,'시제 (since)','Mr. Park ___ for Daeyang Motors [[since 2019]].',['will work','works','worked','has worked'],'D',
 [f'{C(1)} since + 과거 시점 → 그때부터 지금까지 = <b>현재완료</b> has p.p.'],
 '오답: worked(과거 — since와 함께 못 써요) · works(현재) · will work(미래)',
 '<b>since + 시점 · for + 기간</b> → have/has + p.p.','has worked since 2019 = 2019년부터 일해 왔다',2),
(8,'태 (수동)','[[The new conveyor belt]] ___ [[next Monday]] by a team of engineers.',['installing','installs','will install','will be installed'],'D',
 [f'{C(1)} 벨트는 설치<b>되는</b> 것 → <b>수동태</b> (뒤에 by + 사람)', f'{C(2)} next Monday → 미래 → <b>will be p.p.</b>'],
 '오답: will install(벨트가 설치한다? 능동) · installs · installing',
 '빈칸 뒤 <b>목적어 없음 + by ~</b> → 수동태','will be installed = 설치될 것이다',2),
(9,'수일치 (수식어 함정)','[[The instructions]] [[for the new machine]] ___ written in three languages.',['are','is','has','being'],'A',
 [f'{C(2)} for the new machine = 꾸며 주는 말 → <b>괄호</b> 치기', f'진짜 주어 {C(1)} <b>instructions</b> = 복수 → <b>are</b>'],
 '함정 is: 바로 앞 machine(단수)에 끌림. has(능동 — 설명서가 썼다?) · being(동사 자리 ✕)',
 '주어와 동사 사이 <b>전치사 덩어리는 괄호</b> 치고 진짜 주어 찾기','The instructions (for ~) are',3),
(10,'어휘 짝꿍','The team worked late to ___ [[the project deadline]].',['join','fill','meet','attend'],'C',
 [f'{C(1)} deadline과 짝 → <b>meet</b> a deadline = 마감을 지키다'],
 '오답: attend(참석하다 — 회의·수업) · join(함께하다) · fill(채우다)',
 '토익 짝꿍: <b>meet a deadline</b> · place an order · fill out a form','meet a deadline = 마감을 지키다',2),
(11,'어휘 (명사)','Please show your employee ___ [[card]] at the front gate.',['introduction','instruction','information','identification'],'D',
 [f'{C(1)} 정문에서 보여 주는 카드 → <b>신분증</b> = identification card (ID card)'],
 '오답: introduction(소개) · instruction(지시, 설명) · information(정보)',
 '명사 + 명사 덩어리(복합명사)는 <b>통째로</b> 외우기: ID card · safety zone','identification card = 신분증',2),
(12,'숫자 앞 부사','The company hired ___ [[30 new workers]] this year.',['lately','nearly','closely','hardly'],'B',
 [f'{C(1)} 숫자 앞 빈칸 → "<b>거의, 약</b>" = nearly'],
 '오답: lately(최근에) · closely(밀접하게) · hardly(거의 ~않는 — 뜻이 반대)',
 '<b>숫자 앞</b> 빈칸 = nearly · approximately · about · almost','nearly 30 = 거의 30',2),
(13,'어휘 (형용사)','Only ___ [[staff members]] are [[allowed to enter]] the server room.',['automatic','accurate','authorized','annual'],'C',
 [f'{C(1)} staff members와 짝 + {C(2)} 들어가도록 허락됨 → <b>권한을 받은</b> = authorized'],
 '오답: automatic(자동의) · accurate(정확한) · annual(매년의) — 모두 a로 시작해 헷갈리게 만든 보기',
 '형용사 어휘는 <b>뒤 명사</b> + 문장 뜻(Only, allowed)으로 확인','authorized staff only = 관계자 외 출입 금지',3),
(14,'어휘 (동사)','The store will ___ [[a full refund]] if the product arrives damaged.',['offer','spend','ask','suggest'],'A',
 [f'{C(1)} refund와 짝 → <b>offer</b> a refund = 환불해 주다'],
 '오답: spend(돈·시간을 쓰다) · ask(요청하다 — 가게가 환불을 요청?) · suggest(제안하다)',
 '어휘 문제는 <b>빈칸 + 목적어</b>를 한 덩어리로 읽어 보기','offer a full refund = 전액 환불해 주다',2),
(15,'어휘 (부사)','The printer on this floor is ___ out of order, [[so please use the one on the second floor]].',['currently','finally','previously','rarely'],'A',
 [f'{C(1)} 결과: 2층 것을 쓰세요 → <b>지금</b> 고장 = currently'],
 '오답: previously(이전에 — is와 시제가 안 맞음) · rarely(거의 ~않는 — 뜻 반대) · finally(마침내)',
 '<b>so 뒤 결과 문장</b>과 뜻이 맞는 부사 고르기','currently = 현재, 지금',2),
(16,'전치사 vs 접속사','___ [[the heavy rain]], the outdoor event was held as planned.',['Although','Because','Despite','Unless'],'C',
 [f'{C(1)} 빈칸 뒤 = <b>명사구</b>(주어+동사 없음) → <b>전치사</b>', '비가 왔는데도 열림 → 반대 = <b>Despite</b>'],
 '오답: Although · Because · Unless는 모두 접속사(뒤에 주어 + 동사)',
 '<b>빈칸 뒤를 먼저</b>: 명사만 → 전치사 / 주어+동사 → 접속사','despite + 명사 / although + 주어 + 동사',2),
(17,'전치사 vs 접속사','___ [[the machine is]] old, it still works well.',['Because of','Even though','Despite','In spite of'],'B',
 [f'{C(1)} 빈칸 뒤 = <b>주어 + 동사</b>(the machine is) → <b>접속사</b>', '낡았는데도 잘 작동 → 반대 = <b>Even though</b>'],
 '오답: Despite · In spite of · Because of는 모두 전치사(뒤에 명사만)',
 '같은 뜻 짝: despite(전) / although · even though(접)','even though + 주어 + 동사 = ~인데도',2),
(18,'instead of vs rather than','The team decided to repair the old machine ___ [[buying]] a new one.',['in order to','instead of','rather','so that'],'B',
 [f'{C(1)} 빈칸 뒤 <b>-ing</b>(buying) → <b>instead of</b>', '2일차 13번은 반대였어요: 뒤가 동사원형(take) → rather than'],
 '오답: rather(혼자서는 ✕ — rather than이어야 해요) · in order to(+동사원형) · so that(+주어+동사)',
 '<b>instead of + 명사/-ing</b> · rather than + 앞과 같은 모양','instead of buying = 사는 대신',3),
(19,'재귀대명사','[[Ms. Kim and her team]] finished the sales report [[by]] ___.',['they','their','them','themselves'],'D',
 [f'{C(2)} by + <b>-self</b> = 혼자 힘으로, 스스로', f'{C(1)} Ms. Kim and her team = 복수 → <b>themselves</b>'],
 '함정 them: by them이면 "그들에 의해" — 다른 사람이 끝낸 것처럼 돼요. they · their ✕',
 '<b>by oneself</b> = 혼자서 (by myself · by herself · by themselves)','by themselves = 그들 스스로',2),
(20,'비교급 강조',"This year's sales were ___ [[higher than]] last year's.",['far','most','more','very'],'A',
 [f'{C(1)} 비교급(higher than) 앞 강조 → <b>far</b> (훨씬)'],
 '함정 very: 원급만 꾸며요(very high ○, very higher ✕). more(higher에 more 중복) · most(최상급)',
 '비교급 강조: <b>much · far · even · still</b> (very ✕)','far higher = 훨씬 더 높은',1),
]

# ---------------- Part 6 / 7 passages ----------------
PA_HEAD = f'''<table class="mail"><tr><th>To</th><td>All New Employees</td></tr><tr><th>From</th><td>Human Resources</td></tr>
<tr><th>Date</th><td>November 18</td></tr><tr><th>Subject</th><td>Forklift safety training</td></tr></table>'''
PA_BODY = f'''<p>Dear New Employees,</p>
<p><span class="sen" id="s1">Our forklift safety training, {H('orig','originally scheduled for November 25')}, {B(21,'has been moved')} {H('dec','to December 2')}.</span>
<span class="sen" id="s2">{H('trainer','The trainer, Ms. Han,')} has a scheduling conflict on {H('odate','the original date')}.</span>
<span class="sen" id="s3">{B(22,'She will be speaking at a conference in Daegu that day.','long')}</span>
<span class="sen" id="s4">The session will take place in Room 204 from 9 A.M. to noon.</span></p>
<p><span class="sen" id="s5">{H('imp','It is important that')} {H('every','every new employee')} {B(23,'complete')} this session before driving a forklift.</span>
<span class="sen" id="s6">{B(24,'However')}, {H('seats','only 15 seats are available')}.</span>
<span class="sen" id="s7">Please sign up on the HR page by November 28.</span></p>
<p>Human Resources</p>'''
PASSAGE_A = f'<div class="doc"><div class="dockind">E-MAIL</div>{PA_HEAD}<div class="ptext">{PA_BODY}</div></div>'

PC_BODY = f'''<p><span class="sen" id="c1">The north parking lot will be repaved from December 7 to December 11.</span>
<span class="sen" id="c2">During this time, employees should park in the south lot or at the Riverside Sports Center across the street.</span>
<span class="sen" id="c3">{B(25,'Free')} {H('shuttle','shuttle buses')} will run between the sports center and the main gate every 15 minutes.</span></p>
<p><span class="sen" id="c4">Please follow the directions of the security staff {B(26,'while')} {H('sv','you are')} in {H('south','the south lot')}.</span>
<span class="sen" id="c5">{B(27,'Spaces there tend to fill up quickly, so please arrive early.','long')}</span>
<span class="sen" id="c6">After the work is finished, the north lot will have 40 more parking spaces.</span>
<span class="sen" id="c7">We {B(28,'appreciate')} {H('coop','your cooperation')}.</span></p>'''
PASSAGE_C = f'<div class="doc"><div class="dockind">NOTICE</div><div class="ttitle big">Parking Notice for All Employees</div><div class="ptext">{PC_BODY}</div></div>'

PD_BODY = f'''<p><span class="sen" id="d1">SONGTAN (November 18) — Hanul Electronics announced on Monday that it {B(29,'will open')} its second factory in Pyeongtaek {H('spring','next spring')}.</span>
<span class="sen" id="d2">The company's first factory, which opened in 2021, can no longer keep up with growing orders for its battery parts.</span></p>
<p><span class="sen" id="d3">The new building will be twice as large and {H('highly','highly')} {B(30,'automated')}.</span>
<span class="sen" id="d4">{B(31,'However, it will still need many skilled people to run its machines.','long')}</span>
<span class="sen" id="d5">{H('hire','The company plans to hire about 200 workers')}, many of them graduates of local technical high schools.</span>
<span class="sen" id="d6">{B(32,'In addition')}, {H('train','Hanul will provide a six-week paid training program for all new hires')}.</span></p>'''
PASSAGE_D = f'<div class="doc"><div class="dockind">ARTICLE</div><div class="ttitle big">Hanul Electronics to Build Second Factory</div><div class="ptext">{PD_BODY}</div></div>'

CHAT = [('Mina Lee','9:02 A.M.',f"Daniel, {H('broken',"the printer in the design office isn't working again")}."),
('Daniel Cho','9:03 A.M.',"Did you try turning it off and on again?"),
('Mina Lee','9:04 A.M.',f"Twice. And {H('need',"I need 30 copies of the brochure for the 11 o'clock client meeting")}."),
('Daniel Cho','9:05 A.M.',H('free','The one on the third floor is free right now.')),
('Mina Lee','9:06 A.M.',f"Good idea. {H('head',"I'll head up there now.")} {H('call','Could you call the repair company for me?')}"),
('Daniel Cho','9:07 A.M.',H('sure',"Sure, I'll do that right away."))]
SPEAKER2 = 'Daniel'
PASSAGE_E = '<div class="doc chatdoc"><div class="dockind">TEXT MESSAGES</div>' + ''.join(f'<div class="msg {"r" if n.startswith(SPEAKER2) else ""}"><div class="mh"><b>{n}</b> [{t}]</div><div class="bub">{m}</div></div>' for n,t,m in CHAT) + '</div>'

PF_BODY = f'''<p><span class="sen" id="n1">Starting December 1, {H('hours','the fitness center on the second floor of Building D will open at 6:00 A.M., one hour earlier than before')}.</span>
<span class="sen" id="n2">It will continue to close at 9:00 P.M.</span>
<span class="sen" id="n3">The change was made because many employees on the morning shift asked for {H('morning','more time to exercise before work')}.</span></p>
<p><span class="sen" id="n4">{H('towels','Towels')} and {H('lockers','lockers')} will still be provided free of charge.</span>
<span class="sen" id="n5">Please note that {H('pool','the swimming pool will remain closed for repairs until January')}.</span>
<span class="sen" id="n6">Employees must show their {H('id','ID cards')} at the front desk to enter.</span>
<span class="sen" id="n7">Any questions about the new hours can be {H('directed','directed')} to Ms. Park at extension 3021.</span></p>'''
PASSAGE_F = f'<div class="doc"><div class="dockind">NOTICE</div><div class="ttitle big center">Employee Fitness Center — New Hours</div><div class="ptext">{PF_BODY}</div></div>'

PB_HEAD = '''<table class="mail"><tr><th>To</th><td>All Staff</td></tr><tr><th>From</th><td>Kevin Shin, Human Resources</td></tr>
<tr><th>Date</th><td>November 16</td></tr><tr><th>Subject</th><td>Winter skill courses</td></tr></table>'''
PB_BODY = f'''<p>Dear Staff,</p>
<p><span class="sen" id="t1">We are pleased to offer four short courses this winter.</span>
<span class="sen" id="t2">{H('freec','All courses are free')}, but space in each class is limited.</span>
<span class="sen" id="t3">Employees who work in {H('assembly','the assembly area')} are especially encouraged to take {H('robot','the robot maintenance course')}, since {H('newrobots','three new robots will be installed there in January')}.</span>
<span class="sen" id="t4">To register, please send me an e-mail with the name of the course by November 30.</span>
<span class="sen" id="t5">Please note that courses with {H('five','fewer than five registrations')} may be canceled.</span></p>
<p>Kevin Shin</p>'''
ROWS = [('excel','Basic Excel','December 8','Room 101'),('robot','Robot Maintenance','December 10','Room 205'),
        ('eng','Workplace English','December 15','Room 101'),('safe','Safety Leadership','December 17','Room 302')]
TABLE = ('<div class="doc tbl"><div class="dockind">TABLE</div><div class="ttitle">Winter Skill Courses</div><table class="spec"><tr><th>Course</th><th>Date</th><th>Room</th></tr>'
  + ''.join(f'<tr class="hl" id="r{k}"><td><span class="hl" id="c{k}">{c}</span></td><td><span class="hl" id="d{k}">{d}</span></td><td><span class="hl" id="m{k}">{m}</span></td></tr>' for k,c,d,m in ROWS) + '</table></div>')
PASSAGE_B = f'<div class="pairdocs"><div class="doc"><div class="dockind">E-MAIL</div>{PB_HEAD}<div class="ptext">{PB_BODY}</div></div>{TABLE}</div>'

PASS = {'A':PASSAGE_A,'B':PASSAGE_B,'C':PASSAGE_C,'D':PASSAGE_D,'E':PASSAGE_E,'F':PASSAGE_F}
SETTITLE = {'A':'21–24번 · 이메일','C':'25–28번 · 공지','D':'29–32번 · 기사','E':'33–34번 · 문자 대화','F':'35–37번 · 공지','B':'38–40번 · 이메일 + 표'}
SETPART = {'A':6,'C':6,'D':6,'E':7,'F':7,'B':7}
SETINTRO = {'A':'Questions 21-24 refer to the following e-mail.','C':'Questions 25-28 refer to the following notice.',
 'D':'Questions 29-32 refer to the following article.','E':'Questions 33-34 refer to the following text-message chain.',
 'F':'Questions 35-37 refer to the following notice.','B':'Questions 38-40 refer to the following e-mail and table.'}
ORDER = {'A':[21,22,23,24],'C':[25,26,27,28],'D':[29,30,31,32],'E':[33,34],'F':[35,36,37],'B':[38,39,40]}

TL = lambda a,al,b,bl,arrow: (f'<div class="timeline"><div class="tl-bar"></div><div class="tl-pt" style="left:6%"><i></i><b>{a}</b><span>{al}</span></div>'
    f'<div class="tl-pt fut" style="left:66%"><i></i><b>{b}</b><span>{bl}</span></div><div class="tl-arrow">{arrow}</div></div>')
FLOW = lambda a,b,c: f'<div class="flow"><div class="fbox">{a}</div><div class="fdown">↓</div><div class="fbox ans">{b}</div><div class="fdown">↓</div><div class="fbox">{c}</div></div>'
PAIR = lambda a,op,b: f'<div class="pair"><span>{a}</span><em>{op}</em><span>{b}</span></div>'
REL = lambda a,mid,b: f'<div class="rel"><div class="fbox">{a}</div><div class="relmid">{mid}</div><div class="fbox">{b}</div></div>'
CHECK = lambda items: '<div class="check">' + ''.join(f'<div class="{"ok" if ok else "no"}">{"✓" if ok else "✕"} {t}</div>' for ok,t in items) + '</div>'

Q = [
dict(set='A', n=21, tag='문맥 시제 · 태', part=6, cur='b21', fill=1, focus=['s1'], star=3,
  stem='빈칸 (21)에 알맞은 것은?', opts=['has been moved','to move','moving','was moving'], ans='A',
  hl=[('orig',2,'y','1'),('dec',2,'y','2')],
  expl=[(2,f'교육(training)은 스스로 옮기는 게 아니라 <b>옮겨지는</b> 것 → <b>수동태</b> be p.p.'),
        (2,TL(f'{C(1)} 원래','11/25',f'{C(2)} 지금','12/2로 바뀐 상태','바뀐 결과가 지금까지 → has been p.p.')),
        (3,'오답: was moving(교육이 직접 옮기는 중?) · moving · to move(혼자서는 동사 자리에 못 와요)')],
  tip='빈칸 뒤에 <b>목적어가 없고</b>, 주어가 "당하는" 쪽이면 수동태. 바뀐 결과가 지금도 이어지면 <b>has been p.p.</b>', memo='be moved to ~ = ~로 옮겨지다(변경되다)'),
dict(set='A', n=22, tag='문장 삽입', part=6, cur='b22', fill=1, focus=None, star=2,
  stem='빈칸 (22)에 들어갈 문장은?', opts=['Forklift licenses must be renewed every three years.','New employees will receive their uniforms next week.','The forklifts in Warehouse 2 were replaced last month.','She will be speaking at a conference in Daegu that day.'], ans='D',
  hl=[('trainer',2,'y','1'),('odate',2,'y','2'),('b22',2,'g')],
  expl=[(2,f'<b>앞 문장</b>: {C(1)} 강사가 {C(2)} 원래 날짜에 일정이 겹침 → <b>이유</b>가 이어져야 해요.'),
        (2,FLOW('강사 Ms. Han, 원래 날짜에 일정이 겹침',f'(22) <b>She</b>(=강사)는 <b>that day</b>(=원래 날짜)에 학회 발표','교육은 204호, 오전 9시~정오')),
        (3,'오답 (A) 면허 · (B) 유니폼 · (C) 지게차 교체 → <b>일정이 겹친 이유</b>와 연결 ✕')],
  tip='문장 삽입은 보기 속 <b>She · that day</b> 같은 지시어가 앞 문장의 무엇을 가리키는지 확인!', memo='scheduling conflict = 일정이 겹침'),
dict(set='A', n=23, tag='that절 + 동사원형', part=6, cur='b23', fill=1, focus=['s5'], star=2,
  stem='빈칸 (23)에 알맞은 것은?', opts=['completing','complete','completes','completed'], ans='B',
  hl=[('imp',2,'y','1'),('every',2,'b','2')],
  expl=[(2,f'{C(1)} <b>It is important that</b> + 주어 + <b>동사원형</b>'),
        (2,PAIR(f'{C(2,"b")} every new employee (단수)','→','그래도 completes ✕ · <b>complete</b> ○')),
        (3,'함정 completes: 주어가 단수라 -s를 붙이고 싶어져요. completing · completed는 동사 자리 ✕')],
  tip='important · necessary · essential · require <b>that</b> → 주어가 단수여도 <b>동사원형</b>(-s 없음)', memo='It is important that + 주어 + 동사원형'),
dict(set='A', n=24, tag='흐름 (접속부사)', part=6, cur='b24', fill=1, focus=['s5','s6'], star=2,
  stem='빈칸 (24)에 알맞은 것은?', opts=['Therefore','However','For example','Similarly'], ans='B',
  hl=[('imp',2,'y','1'),('seats',2,'b','2')],
  expl=[(2,'앞뒤 문장을 한 줄씩 요약해서 <b>관계</b>를 먼저 정해요.'),
        (2,REL(f'{C(1)} 신입은 <b>모두</b> 꼭 들어야 해요','반대<br>↔',f'{C(2,"b")} 그런데 자리는 <b>15석뿐</b>')),
        (3,'반대 → <b>However</b>. Therefore(그래서) · For example(예를 들어) · Similarly(비슷하게)는 관계가 달라요.')],
  tip='접속부사: 보기보다 먼저 <b>앞뒤 관계(반대 · 결과 · 추가 · 예시)</b>를 한 단어로 정하기', memo='반대 However · 결과 Therefore · 추가 In addition'),

dict(set='C', n=25, tag='어휘 (형용사)', part=6, cur='b25', fill=1, focus=['c3'], star=1,
  stem='빈칸 (25)에 알맞은 것은?', opts=['Empty','Clear','Free','Open'], ans='C',
  hl=[('shuttle',2,'y','1')],
  expl=[(2,f'{C(1)} shuttle buses와 짝 → 직원들을 위한 <b>무료</b> 셔틀버스'),
        (2,PAIR('<b>free</b> shuttle bus','=','무료 셔틀버스')),
        (3,'오답: Empty(텅 빈) · Clear(맑은, 분명한) · Open(열린) — 버스를 꾸미기엔 뜻이 어색해요.')],
  tip='free = 무료의 / 한가한 · 비어 있는(사용 가능한) — <b>뜻이 두 개</b>! 33번에서 또 나와요.', memo='free shuttle bus = 무료 셔틀버스'),
dict(set='C', n=26, tag='전치사 vs 접속사', part=6, cur='b26', fill=1, focus=['c4'], star=2,
  stem='빈칸 (26)에 알맞은 것은?', opts=['during','despite','because of','while'], ans='D',
  hl=[('sv',2,'y','1')],
  expl=[(2,f'{C(1)} 빈칸 뒤 = <b>주어 + 동사</b>(you are) → <b>접속사</b>'),
        (2,PAIR('<b>while</b> + 주어 + 동사','=','~하는 동안')),
        (3,'함정 during: 뜻은 "~동안"으로 같지만 <b>전치사</b>(during the work ○). despite · because of도 전치사')],
  tip='같은 뜻 짝: <b>during(전) / while(접)</b> · despite / although · because of / because', memo='while you are ~ / during your stay'),
dict(set='C', n=27, tag='문장 삽입', part=6, cur='b27', fill=1, focus=None, star=3,
  stem='빈칸 (27)에 들어갈 문장은?', opts=['Spaces there tend to fill up quickly, so please arrive early.','The north lot was first built in 2010.','Employees may also work from home on Fridays.','The sports center offers a discount to all employees.'], ans='A',
  hl=[('south',2,'y','1'),('b27',2,'g')],
  expl=[(2,f'보기 (A)의 <b>there</b>(그곳)가 가리킬 장소가 바로 앞에 있어야 해요 → {C(1)} <b>the south lot</b>'),
        (2,FLOW('남쪽 주차장에서는 보안요원 안내를 따르세요',f'(27) <b>그곳</b>(=남쪽 주차장)은 금방 차니 일찍 오세요','공사가 끝나면 북쪽 주차장 40면 늘어남')),
        (3,'오답 (B) 지어진 해 · (C) 재택근무 · (D) 체육센터 할인 → 주차 이야기 흐름에서 벗어나요.')],
  tip='보기 속 <b>there · it · they · this</b>가 들어 있으면, 바로 앞 문장에서 가리킬 대상을 찾기', memo='fill up quickly = 금방 차다'),
dict(set='C', n=28, tag='어휘 (동사)', part=6, cur='b28', fill=1, focus=['c7'], star=2,
  stem='빈칸 (28)에 알맞은 것은?', opts=['apologize','deserve','expect','appreciate'], ans='D',
  hl=[('coop',2,'y','1')],
  expl=[(2,f'공지 마지막 인사 + {C(1)} your cooperation(협조) → <b>감사합니다</b>'),
        (2,PAIR('We <b>appreciate</b> your cooperation.','=','협조에 감사드립니다')),
        (3,'함정 apologize: apologize <b>for</b> ~ 처럼 for가 필요해요. deserve(~을 받을 만하다) · expect(기대하다)')],
  tip='공지·이메일 마지막 문장 단골: <b>We appreciate your cooperation / patience.</b>', memo='appreciate = 감사하다 (뒤에 바로 명사)'),

dict(set='D', n=29, tag='문맥 시제', part=6, cur='b29', fill=1, focus=['d1'], star=2,
  stem='빈칸 (29)에 알맞은 것은?', opts=['has opened','opened','will open','was opening'], ans='C',
  hl=[('spring',2,'y','1')],
  expl=[(2,f'같은 문장 끝 {C(1)} <b>next spring</b>(내년 봄) → 아직 안 일어난 일 = <b>미래</b>'),
        (2,TL('11/18','기사 날짜',f'{C(1)} 내년 봄','2공장 개장','앞으로 일어날 일 → will')),
        (3,'오답: has opened · opened · was opening — 모두 이미 일어난 일이라 next spring과 맞지 않아요.')],
  tip='시제 문제는 <b>시간 표현</b>(next · last · since · by)을 먼저 찾기', memo='next spring + will 동사원형'),
dict(set='D', n=30, tag='분사형용사 (-ed)', part=6, cur='b30', fill=1, focus=['d3'], star=3,
  stem='빈칸 (30)에 알맞은 것은?', opts=['automation','automated','automate','automatically'], ans='B',
  hl=[('highly',2,'y','1')],
  expl=[(2,f'{C(1)} be + 부사(highly) + 빈칸 → 형용사 자리. 부사 highly는 지우고 보기!'),
        (2,PAIR('건물은 자동화<b>된</b> 것','→','<b>automated</b> (-ed)')),
        (3,'오답: automation(명사) · automate(동사) · automatically(부사 — 부사 highly 뒤에 또 부사 ✕)')],
  tip='be와 빈칸 사이 <b>부사는 지우고</b> 보기. 사물이 "~된" 상태면 <b>-ed</b>', memo='highly automated = 고도로 자동화된'),
dict(set='D', n=31, tag='문장 삽입', part=6, cur='b31', fill=1, focus=None, star=3,
  stem='빈칸 (31)에 들어갈 문장은?', opts=['Pyeongtaek is home to several large companies.','Its first factory was built by a local company.','However, it will still need many skilled people to run its machines.','Battery parts are mainly exported to Europe.'], ans='C',
  hl=[('highly',2,'y','1'),('hire',2,'y','2'),('b31',2,'g')],
  expl=[(2,f'앞: {C(1)} 고도로 <b>자동화</b> → 사람이 덜 필요할 것 같은데… 뒤: {C(2)} <b>200명 채용</b>'),
        (2,FLOW('공장이 크고 고도로 자동화됨','(31) <b>However</b>, 그래도 기계를 돌릴 숙련 인력이 많이 필요','200명 채용, 지역 마이스터고 졸업생 다수')),
        (3,'오답 (A) 평택의 대기업 · (B) 1공장 건설사 · (D) 수출 지역 → 자동화와 채용을 <b>이어 주지 못해요.</b>')],
  tip='보기에 <b>However</b>가 있으면 앞 문장과 <b>반대</b>되는 내용인지 확인. 앞뒤를 이어 주는 문장이 정답!', memo='skilled people = 숙련된 인력'),
dict(set='D', n=32, tag='흐름 (접속부사)', part=6, cur='b32', fill=1, focus=['d5','d6'], star=2,
  stem='빈칸 (32)에 알맞은 것은?', opts=['However','Otherwise','In addition','Instead'], ans='C',
  hl=[('hire',2,'y','1'),('train',2,'b','2')],
  expl=[(2,'앞뒤 관계부터 정해요.'),
        (2,REL(f'{C(1)} 200명을 뽑을 거예요','추가<br>+',f'{C(2,"b")} 6주 유급 연수도 해 줘요')),
        (3,'좋은 소식에 좋은 소식을 <b>더함</b> → In addition. However(반대) · Otherwise(그렇지 않으면) · Instead(대신에)')],
  tip='앞뒤가 <b>같은 방향</b>으로 더해지면 In addition · Also · Moreover', memo='In addition = 게다가'),

dict(set='E', n=33, tag='의도 파악', part=7, cur=None, fill=None, focus=None, star=2,
  stem='At 9:05 A.M., what does Mr. Cho most likely mean when he writes, <span class="kw">"The one on the third floor is free right now"</span>?',
  opts=['A coworker on the third floor can help with the design.','The repair service does not cost anything.','A meeting room on the third floor is available.','Ms. Lee can use another printer.'], ans='D',
  hl=[('broken',2,'y','1'),('free',2,'b'),('head',2,'y','2')],
  expl=[(2,f'{C(1)} 프린터가 고장 → <b>The one</b> = 다른 <b>프린터</b>, free = <b>비어 있는(쓸 수 있는)</b>'),
        (2,f'{C(2)} 바로 뒤 Mina: "좋은 생각, 지금 올라갈게요" → 3층 프린터를 쓰러 감'),
        (3,'함정 (B) free = "<b>무료</b>"로 읽으면 수리비가 무료? — 25번의 free와 다른 뜻! (A)(C) 동료·회의실은 대화에 없어요.')],
  tip='의도 파악은 따옴표 문장 <b>바로 앞 말 + 바로 뒤 말</b>로. <b>쉬운 단어의 다른 뜻</b>(free · stand)을 조심!', memo='free = 무료의 / 비어 있는, 사용 가능한'),
dict(set='E', n=34, tag='다음 할 일', part=7, cur=None, fill=None, focus=None, star=2,
  stem='What will <span class="kw">Mr. Cho</span> most likely do <span class="kw">next</span>?', opts=['Contact a repair company','Print the brochures','Go to the third floor','Meet the client'], ans='A',
  hl=[('call',2,'y','1'),('sure',2,'y','2'),('head',3,'r')],
  expl=[(2,f'{C(1)} Mina의 부탁: "수리 업체에 전화해 줄래요?" → {C(2)} Daniel: "네, 바로 할게요"'),
        (2,PAIR('call the repair company','⇄','Contact a repair company')),
        (3,'함정 (C) 3층에 가는 사람은 <b>Mina</b>예요. (B) 브로슈어 인쇄도 Mina의 일.')],
  tip='"다음에 할 일"은 그 사람의 <b>마지막 말</b>(Sure, I\'ll ~)과 그 앞 부탁을 함께 보기', memo='call = contact (연락하다)'),

dict(set='F', n=35, tag='목적', part=7, cur=None, fill=None, focus=None, star=2,
  stem='What is the <span class="kw">purpose</span> of the notice?', opts=['To ask employees to take a survey','To announce new opening hours','To introduce a new swimming pool','To explain how to get an ID card'], ans='B',
  hl=[('hours',2,'y','1'),('pool',3,'r'),('id',3,'r')],
  expl=[(2,f'제목 New Hours + 첫 문장 {C(1)} 12월 1일부터 오전 6시에 문을 연다'),
        (2,PAIR('open at 6:00 A.M., one hour earlier','⇄','new opening hours')),
        (3,'함정 (C) 수영장은 새로 생기는 게 아니라 <b>수리 중</b>. (D) 신분증은 "보여 줘야 한다"는 말뿐. (A) 설문 언급 없음')],
  tip='목적 문제는 <b>제목 + 첫 문장</b>! 지문 단어(pool · ID)가 들어간 보기는 함정일 때가 많아요.', memo='opening hours = 운영 시간'),
dict(set='F', n=36, tag='NOT', part=7, cur=None, fill=None, focus=None, star=2,
  stem='What is <span class="kw">NOT</span> available at the fitness center in December?', opts=['Lockers','Towels','The swimming pool','Early-morning exercise'], ans='C',
  hl=[('towels',2,'g'),('lockers',2,'g'),('hours',2,'g'),('pool',2,'r')],
  expl=[(2,CHECK([(True,'(A) Lockers — 4번째 문장'),(True,'(B) Towels — 4번째 문장'),(True,'(D) Early-morning exercise — 오전 6시 개장'),(False,'(C) the swimming pool will remain <b>closed</b> until January')])),
        (3,'지문에 <b>있는 것 3개를 지우면</b> 남는 하나가 정답이에요.')],
  tip='NOT 문제는 보기마다 지문 위치를 찾아 ✓ 표시 → 못 찾거나 반대로 나온 것이 정답', memo='remain closed = 계속 닫혀 있다'),
dict(set='F', n=37, tag='동의어 (다의어)', part=7, cur=None, fill=None, focus=['n7'], star=3,
  stem='The word <span class="kw">"directed"</span> in paragraph 2 is closest in meaning to', opts=['sent','ordered','managed','pointed'], ans='A',
  hl=[('directed',2,'y','1')],
  expl=[(2,'그 자리에 보기를 넣어 보기: "Any questions … can be ___ to Ms. Park"'),
        (2,CHECK([(True,'sent — 질문을 Ms. Park에게 <b>보내다</b>(문의하다)'),(False,'ordered — 질문을 명령받다?'),(False,'managed — 질문을 관리받다?'),(False,'pointed — 질문을 가리키다?')])),
        (3,'함정 (B)(C): direct의 다른 뜻 "지시하다 · 감독하다"에 끌려요. 문장 속 뜻으로 골라야 해요.')],
  tip='동의어 문제는 <b>사전 첫 뜻이 함정</b>! 그 자리에 보기를 넣어 문장 뜻으로 고르기', memo='questions can be directed to ~ = 문의는 ~에게'),

dict(set='B', n=38, tag='사실 확인', part=7, cur=None, fill=None, focus=None, star=2,
  stem='What is indicated about <span class="kw">the courses</span>?', opts=['They are only for new employees.','They are free of charge.','They will be held in January.','They are taught online.'], ans='B',
  hl=[('freec',2,'y','1'),('newrobots',3,'r')],
  expl=[(2,f'근거: {C(1)} <b>All courses are free</b>'),
        (2,PAIR('All courses are free','⇄','They are free of charge.')),
        (3,'함정 (C) <b>January</b>는 지문에 있지만 로봇이 <b>설치되는</b> 때예요. 강좌는 12월(표). (A)(D) 언급 없음')],
  tip='사실 확인은 보기를 하나씩 지문과 대조! <b>지문 단어가 그대로 들어간 보기</b>는 무슨 이야기였는지 다시 확인', memo='free of charge = 무료로'),
dict(set='B', n=39, tag='추론', part=7, cur=None, fill=None, focus=None, star=2,
  stem='What is suggested about <span class="kw">the assembly area</span>?', opts=['It will be closed in December.','It is located in Room 205.','It will get new equipment soon.','It has fewer than five workers.'], ans='C',
  hl=[('newrobots',2,'y','1'),('mrobot',3,'r'),('five',3,'r')],
  expl=[(2,f'{C(1)} 새 로봇 3대가 1월에 <b>there</b>(=조립 구역)에 설치됨'),
        (2,PAIR('three new robots will be installed there','⇄','It will get <b>new equipment</b> soon.')),
        (3,'함정 (B) <b>Room 205</b>는 로봇 정비 <b>강좌</b>가 열리는 곳(표). (D) five는 강좌 <b>신청 인원</b> 이야기예요.')],
  tip='추론은 지문의 말을 <b>다른 말로 바꾼 보기</b>(robots → equipment)가 정답일 때가 많아요', memo='equipment = 장비 (robots, machines)'),
dict(set='B', n=40, tag='연계 (이메일 + 표)', part=7, cur=None, fill=None, focus=None, star=3,
  stem='An employee in the assembly area follows Mr. Shin\'s suggestion. <span class="kw">When</span> will the employee most likely attend a course?', opts=['December 8','December 10','December 15','December 17'], ans='B',
  hl=[('assembly',2,'b','1'),('robot',2,'b','1'),('rrobot',2,'b'),('crobot',2,'b','1'),('drobot',3,'g','2'),('newrobots',4,'r')],
  expl=[(2,f'{C(1,"b")} 이메일: 조립 구역 직원에게 <b>robot maintenance course</b>를 추천'),
        (3,f'{C(2,"g")} 표에서 Robot Maintenance 줄 → 날짜 <b>December 10</b>'),
        (4,'함정: January는 로봇 <b>설치</b> 시기라 강좌 날짜가 아니에요. 표의 다른 날짜(8 · 15 · 17일)도 모두 보기에 있으니 <b>어느 줄인지</b>가 핵심!')],
  tip='연계 문제: 이메일에서 <b>조건</b>(어떤 강좌?)을 찾고 → 표에서 그 <b>줄</b>을 읽기', memo='be encouraged to ~ = ~하도록 권장되다'),
]

GUIDE = {
 'A':'<h3>읽는 순서</h3><ol><li><b>Date · Subject</b> 먼저 → 언제, 무슨 일?</li><li>위에서 아래로 읽다가 빈칸을 만나면 바로 풀기</li><li><b>문장 삽입(22)</b>은 맨 마지막에</li></ol><div class="tipbox">⏱ 실제 시험: 한 지문 약 2분 40초</div>',
 'C':'<h3>읽는 순서</h3><ol><li><b>제목</b> → 무엇에 관한 공지?</li><li>26번은 <b>빈칸 뒤</b>에 주어+동사가 있는지 먼저</li><li><b>문장 삽입(27)</b>은 맨 마지막에</li></ol><div class="tipbox">⏱ 실제 시험: 한 지문 약 2분 40초</div>',
 'D':'<h3>읽는 순서</h3><ol><li><b>날짜(November 18)</b>와 제목 → 무슨 소식?</li><li>시제 빈칸(29)은 <b>시간 표현</b>부터 찾기</li><li><b>문장 삽입(31)</b>은 맨 마지막에</li></ol><div class="tipbox">⏱ 실제 시험: 한 지문 약 2분 40초</div>',
 'E':'<h3>읽는 순서</h3><ol><li><b>질문 2개</b> 먼저 — 의도 파악은 몇 시 메시지?</li><li>두 사람이 각자 <b>무엇을 하기로</b> 했는지 구분</li><li>따옴표 문장은 <b>앞 · 뒤 말풍선</b>과 함께</li></ol><div class="tipbox">⏱ 실제 시험: 2문항 세트 약 1분 30초</div>',
 'F':'<h3>읽는 순서</h3><ol><li><b>질문 3개</b> 먼저 → 키워드 표시</li><li>제목 + 첫 문장 = 글의 목적</li><li>NOT 문제는 보기마다 지문 위치 찾기</li></ol><div class="tipbox">⏱ 실제 시험: 3문항 세트 약 2분</div>',
 'B':'<h3>읽는 순서</h3><ol><li><b>질문 3개</b> 먼저 → 키워드 표시</li><li>이메일: 누가 누구에게, 무엇을 권하나?</li><li>표: 칸 이름(강좌 · 날짜 · 강의실)만 훑기</li><li>연계 문제(40)는 <b>두 지문을 오가며</b></li></ol><div class="tipbox">⏱ 실제 시험: 3문항 세트 약 3분</div>'}
DONE = {
 'A':[('21','has been moved','옮겨진 상태(수동 + 완료)'),('22','강사가 그날 학회 발표','She = 강사'),('23','complete','important that + 원형'),('24','However','반대')],
 'C':[('25','Free','무료 셔틀버스'),('26','while','뒤에 주어 + 동사'),('27','그곳은 금방 차니 일찍','there = 남쪽 주차장'),('28','appreciate','협조에 감사')],
 'D':[('29','will open','next spring'),('30','automated','highly + -ed'),('31','그래도 숙련 인력 필요','자동화 ↔ 채용'),('32','In addition','추가')]}
