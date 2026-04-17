import streamlit as st
import math

st.set_page_config(page_title="계산기 웹앱", page_icon="🧮")

st.title("🧮 다기능 계산기")
st.write("사칙연산, 모듈러, 지수, 로그 연산을 지원합니다.")

# 연산 선택
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

# 입력값
a = st.number_input("첫 번째 숫자", value=1.0)
b = st.number_input("두 번째 숫자", value=1.0)

result = None

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
            st.error("로그의 밑(a)은 0보다 크고 1이 아니어야 하며, 진수(b)는 0보다 커야 합니다.")
        else:
            result = math.log(b, a)

    if result is not None:
        st.success(f"결과: {result}")

except Exception as e:
    st.error(f"오류 발생: {e}")
