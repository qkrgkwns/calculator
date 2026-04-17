import streamlit as st
import math

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

st.title("🧮 다기능 계산기")
st.write("연산을 먼저 선택하면, 필요한 입력값이 안내됩니다.")

# 1️⃣ 연산 먼저 선택
operation = st.selectbox(
    "연산을 선택하세요",
    (
        "덧셈 (+)",
        "뺄셈 (-)",
        "곱셈 (*)",
        "나눗셈 (/)",
        "모듈러 (%)",
        "지수 (x^y)",
        "로그 (logₐ b)"
    )
)

st.divider()

# 2️⃣ 연산에 따라 입력 UI 변경
if operation in ["덧셈 (+)", "뺄셈 (-)", "곱셈 (*)", "나눗셈 (/)", "모듈러 (%)"]:
    a = st.number_input("첫 번째 숫자", value=1.0)
    b = st.number_input("두 번째 숫자", value=1.0)

elif operation == "지수 (x^y)":
    a = st.number_input("밑 (x)", value=2.0)
    b = st.number_input("지수 (y)", value=2.0)

elif operation == "로그 (logₐ b)":
    a = st.number_input("밑 (a)", value=10.0)
    b = st.number_input("진수 (b)", value=100.0)

result = None

st.divider()

# 3️⃣ 계산 버튼
if st.button("계산하기"):
    try:
        if operation == "덧셈 (+)":
            result = a + b

        elif operation == "뺄셈 (-)":
            result = a - b

        elif operation == "곱셈 (*)":
            result = a * b

        elif operation == "나눗셈 (/)":
            if b == 0:
                st.error("0으로 나눌 수 없습니다.")
            else:
                result = a / b

        elif operation == "모듈러 (%)":
            result = a % b

        elif operation == "지수 (x^y)":
            result = a ** b

        elif operation == "로그 (logₐ b)":
            if a <= 0 or a == 1 or b <= 0:
                st.error("로그 조건을 만족해야 합니다. (밑>0, 밑≠1, 진수>0)")
            else:
                result = math.log(b, a)

        if result is not None:
            st.success(f"결과: {result}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
