import google.generativeai as genai
import streamlit as st
import textwrap

# Настройка API-ключа (через Streamlit Secrets)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Параметры модели
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

# Имя модели
model_name = "gemini-exp-1206"  # Используйте "gemini-pro", если не работаете с изображениями

# Создание модели
model = genai.GenerativeModel(model_name=model_name, generation_config=generation_config)

# Инициализация чат-сессии
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Заголовок приложения
st.title("Hello, miracle!")
st.subheader("✦ Official Gemeni API is used")

# Инициализация истории сообщений, если её нет в состоянии сессии
if "messages" not in st.session_state:
    st.session_state.messages = []

# Отображение истории сообщений
for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"]:
        with st.chat_message(message["role"]):
            # Добавляем unsafe_allow_html=True для поддержки LaTeX
            st.markdown(message["content"], unsafe_allow_html=True)

# Обработка ввода пользователя
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        # Добавляем unsafe_allow_html=True для поддержки LaTeX
        st.markdown(prompt, unsafe_allow_html=True)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
                # --- Добавляем анимацию загрузки (спиннер) ---
    with st.spinner("Generating response..."):
        try:
            response = st.session_state.chat_session.send_message(prompt, stream=True)
            for chunk in response:
                full_response += chunk.text
                # Добавляем unsafe_allow_html=True для поддержки LaTeX
                message_placeholder.markdown(full_response + " ⬤", unsafe_allow_html=True)
            # Добавляем unsafe_allow_html=True для поддержки LaTeX
            message_placeholder.markdown(full_response, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            full_response = "Error occurred while generating response."

    st.session_state.messages.append({"role": "assistant", "content": full_response})