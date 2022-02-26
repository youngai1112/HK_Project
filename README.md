# HK_Project

<<<<<<< HEAD

--- 프로젝트 관련 수업 진행
=======
## 0218


--- 프로젝트 관련 수업 진행

>>>>>>> b6690222d389e2a9ea7d13f46b8d1a34f46512c0
1. 아이디어 도출: 인당 1개 이상

2. 아이디어 문제점 파악: 팀원 전체 참여

3. 해결책 제시: 팀원 전체 참여


(예제 1팀 사례)
<<<<<<< HEAD
- 1조 아이디어: 금융 관련 주식 투자 AI
=======

- 1조 아이디어: 금융 관련 주식 투자 AI

>>>>>>> b6690222d389e2a9ea7d13f46b8d1a34f46512c0
기사 텍스트 시퀀스를 읽음 > 신경망 출력 1) 투자 O, 2) 투자 X


- 아이디어 문제점: 
<<<<<<< HEAD
1) 데이터 확보 전략 
2) 데이터 레이블 작업을 직접 해야함 -> but, 데이터의 수가 부족함 

1) -> 네이버 금융에서 확보 가능  
2) 기사 내에 특정 단어를 통해 투자를 할지 말지 레이블 설정을 해야 함
but, 기사에는 target값이 없음
인공지능 데이터 셋: 지도학습 {(x, t)} x: 기사 텍스트 시퀀스 t: 타겟 레이블 (긍정, 부정)
인공지능 learning method: 1) 지도학습 2) 비지도학습(강화학습) 3) 준지도 학습
=> 전이학습(transfer learning) : 기존의 누군가가 비슷한 무언가를 해서 적당한 신경망을 만들어 놓은 것

- 해결책 제시: 
1) 네이버 금융 크롤 가능 
2-1) -> 전이학습 가능성 확인
2-2) 자동(프로그램 or RPA -- 광의의 인공지능) 레이블 가능 여부 (프로그램사용)
2-2.1) 레이블: 투자 O, 투자 X (선택) -- 텍스트 시퀀스의 긍정 / 부정에 따라 레이블 결정
2-2.2) 인공지능 데이터셋: (1) 지도학습 {(x,t)} = {('오스템기사', '투자 X')}

1) (네이버 증권> 시황/전략 카테고리 > XPath 사용해서 기사 크롤링 여부 확인)
li는 같은 형식을 반복 > 크롤링이 가능한 형식인지 확인 > 크롤링이 가능하다!
=======

1) 데이터 확보 전략 

2) 데이터 레이블 작업을 직접 해야함 -> but, 데이터의 수가 부족함 

1) -> 네이버 금융에서 확보 가능 
 
2) 기사 내에 특정 단어를 통해 투자를 할지 말지 레이블 설정을 해야 함

but 기사에는 target값이 없음

인공지능 데이터 셋: 지도학습 {(x, t)} x: 기사 텍스트 시퀀스 t: 타겟 레이블 (긍정, 부정)

인공지능 learning method: 1) 지도학습 2) 비지도학습(강화학습) 3) 준지도 학습

=> 전이학습(transfer learning) : 기존의 누군가가 비슷한 무언가를 해서 적당한 신경망을 만들어 놓은 것

- 해결책 제시: 

1) 네이버 금융 크롤 가능 

2-1) -> 전이학습 가능성 확인

2-2) 자동(프로그램 or RPA -- 광의의 인공지능) 레이블 가능 여부 (프로그램사용)

2-2.1) 레이블: 투자 O, 투자 X (선택) -- 텍스트 시퀀스의 긍정 / 부정에 따라 레이블 결정

2-2.2) 인공지능 데이터셋: (1) 지도학습 {(x,t)} = {('오스템기사', '투자 X')}


1) (네이버 증권> 시황/전략 카테고리 > XPath 사용해서 기사 크롤링 여부 확인)

li는 같은 형식을 반복 > 크롤링이 가능한 형식인지 확인 > 크롤링이 가능하다!

>>>>>>> b6690222d389e2a9ea7d13f46b8d1a34f46512c0
2) 기사에 나와있는 날짜와 시간대 확인 > 해당 회사의 주가를 확인 > 레이블을 자동 설정할 수 있지 않을까??
