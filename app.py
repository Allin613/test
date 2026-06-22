import streamlit as st


# st.title('건강 데이터 탐험기')

# st.write('이 앱은 의료 데이터를 수비게 삽펴보는 도구입니다.')

# name = st.text_input("이름을 입력하세요")

# if name:
#     st.write(f"반갑습니다, {name}님! 함께 시작해요 ")
# else:
#     st.info("위에 이름을 입력하면 인사를 드릴게요.")

# -------------------------------------------------------------------

import pandas as pd

# df = pd.read_csv("heart_failure.csv")

# st.subheader(" 환자 데이터")
# st.dataframe(df.head())

# st.metric(
#     label = '전체 환자 수',
#     value = f"{len(df)}명",
#     delta = "299건 수집"
# )

# -------------------------------------------------------------------

# df = pd.read_csv(r"D:\streamlit_test\heart_failure.csv") # 데이터 불러오기

# st.title('심부전 환자 데이터') # 화면 제목 설정하기

# st.dataframe(df.head(10)) # 데이터프레임 앞 10개 행을 출력하기

# st.metric(label = '전체 환자 수', value = f"{len(df)}명",)

# avg = df['age'].mean() # 일단 계산하고 값 넣어주기

# st.metric("평균 나이", f"{avg:.1f}세") # 지표 표시 metric, 결과 강조 출력


# -------------------------------------------------------------------


# df = pd.read_csv(r"D:\streamlit_test\heart_failure.csv") # 데이터 불러오기

# st.title('심부전 환자 데이터') # 화면 제목 설정하기


# age_max = st.slider("최대 나이", 40, 95, 70) # 40 : 최소, 95 : 최대, 70: 초기

# filtered = df[df['age'] <= age_max]

# st.write(f"{len(filtered)}명이 조건에 맞아요")
# st.dataframe(filtered)


# -------------------------------------------------------------------


# df = pd.read_csv(r"D:\streamlit_test\heart_failure.csv") # 데이터 불러오기

# st.title('심부전 환자 데이터') # 화면 제목 설정하기

# choice = st.selectbox("성별", ["남성", "여성"]) # 사용자 입력받기

# only_death = st.selectbox("사망 환자만 보기")

# # 이거 더 해야해

# code = 1 if choice == '남성' else 0

# result = df[df['sex'] == code] # 내가 선택한 성별에 해당되는 값과 같은 것만 true로 뽑아내겠다. 

# st.dataframe(result)

# st.write(f"{len(result)}명")

# -------------------------------------------------------------------

import matplotlib.pyplot as plt

# df = pd.read_csv(r"D:\streamlit_test\heart_failure.csv") # 데이터 불러오기

# fig, ax = plt.subplots()

# ax.hist(df['age'], bins = 20, color = '#5BAFB8')

# ax.set_xlabel("age")
# ax.set_ylabel("count")

# st.pyplot(fig)


# -------------------------------------------------------------------

# df = pd.read_csv(r"D:\streamlit_test\heart_failure.csv") # 데이터 불러오기

# counts = df['DEATH_EVENT'].value_counts().sort_index()

# # 방법 B — matplotlib
# fig, ax = plt.subplots()

# colors = ["#4CAF50", "#F44336"]

# ax.bar(["survive","death"], counts.values, color=colors)


# st.pyplot(fig)


# -------------------------------------------------------------------


# 왼쪽 사이드바에 필터를 둔다

# df = pd.read_csv(r"D:\streamlit_test\heart_failure.csv") # 데이터 불러오기

# st.sidebar.header(" 필터") # 왼쪽 사이드 바에 필터라는 제목 생성
# age = st.sidebar.slider("최대 나이",40, 95, 70) # 사이드 바에 슬라이드 설정
# df = df[df['age'] <= age] # 데이터 필터링 시행
# # 본문을 둘로 나눈다
# c1, c2 = st.columns(2) # 좌우를 둘로 나눈다
# c1.metric("환자 수", len(df))
# c2.metric("평균 나이", f"{df.age.mean():.0f}")


# -------------------------------------------------------------------


df = pd.read_csv("heart_failure.csv") # 데이터 불러오기

st.sidebar.header(" 필터") # 왼쪽 사이드 바에 필터라는 제목 생성
age = st.sidebar.slider("최대 나이",40, 95, 70) # 사이드 바에 슬라이드 설정
df = df[df['age'] <= age] # 데이터 필터링 시행
# 본문을 둘로 나눈다
c1, c2 = st.columns(2) # 좌우를 둘로 나눈다
c1.metric("환자 수", len(df))
c2.metric("평균 나이", f"{df.age.mean():.0f}")

tab1, tab2 = st.tabs(["표", "차트"])

with tab1:
    st.dataframe(df)
    
with tab2:
    fig, ax = plt.subplots()
    ax.hist(df['age'], bins = 20, color='#F44336')
    st.pyplot(fig)
    
# -------------------------------------------------------------------


# app.py — 이 파일만 실행
# import streamlit as st
# def home(): 
#  st.title("🏠 홈")
# def data():
#  st.title("📊 데이터")
# pg = st.navigation([ 
# st.Page(home, title="홈",
# icon="🏠", default=True),
# st.Page(data, title="데이터",
# icon="📊"),
# ])
# pg.run() 
