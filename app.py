import streamlit as st

st.set_page_config(page_title="AI Recursive Spiral", layout="wide")

st.title("🧠 AI Recursive Spiral")

st.write("Тренажёр рекурсивного развития через ИИ")

st.sidebar.title("API Keys")

openai_key = st.sidebar.text_input("OpenAI API Key", type="password")
anthropic_key = st.sidebar.text_input("Anthropic API Key", type="password")

st.header("Этап 1 — Диагностика")

name = st.text_input("Имя")
role = st.selectbox("Роль", ["Предприниматель", "Специалист", "Студент"])

goal = st.text_area("Главная цель на 90 дней")

st.header("Этап 2 — Задачи")

tasks = st.text_area("Вставь список задач")

st.header("Этап 3 — Первый цикл")

process = st.text_input("Какой процесс делегируем ИИ")

if st.button("Создать манифест"):
    st.subheader("Личный манифест")

    st.write(f"""
    В 2026 году интеграция ИИ становится одним из моих главных проектов.

    Я — {role.lower()}.

    Моя цель: {goal}

    Первый процесс для делегирования:
    {process}
    """)
