# 기초영어반 RC 자료 생성기 (3일차부터)
`_` 로 시작하는 폴더라 GitHub Pages에는 게시되지 않음.
- data3.py : 40문항 데이터(Part 5 목록 P5, Part 6·7 지문 PASS·문항 Q, GUIDE, DONE). 새 일차는 이 파일을 복사해 내용만 교체.
- expl3.py : 해설 화면 HTML (`python3 expl3.py ../../t4/index.html`). css.txt·js.txt 필요, 글꼴 경로 FP 확인.
- pdf3.py  : 문제지 4쪽·교사용 정답표 1쪽 (`python3 pdf3.py E` — E = 그 세트는 첫 문항을 지문과 묶지 않음, 빈칸 조절용)
- review3.py : 복습 노트 2쪽 + 복습 테스트(quiz/index.html, 2일차 페이지를 틀로 사용 — LESSON 값 바꾸기)
- chk.py : 해설 화면 넘침 자동 검사 (.qcard scroll 10px은 원래 있는 값이라 무시)
