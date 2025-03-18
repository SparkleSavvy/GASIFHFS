# 🌠 GASIFHFS - Enhanced

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/DEADS1KE/GASIFHFS)
[![GitHub Repo stars](https://img.shields.io/github/stars/SparkleSavvy/GASIFHFS?style=social)](https://github.com/SparkleSavvy/GASIFHFS)

This open-source project brings the power of Google's Gemini AI to a user-friendly chatbot interface. Interact with the latest Gemini models, explore their capabilities in text generation, conversation, and now with enhanced image understanding!

> [!TIP]
> For better rendering of LaTeX formulas just set the model temperature to 0.20 and insert this system prompt: 
`You are a powerful maths wizard.  Solve the following problems, clearly showing your steps.  Use LaTeX for all mathematical expressions and equations.  If you cannot solve a problem, explain why. Check yourself.`

## ❗ Disclaimer

This project uses a **`beta` branch for active development and pre-release versions (e.g., `v1.0.2-alpha.1`, `v1.0.2-alpha.2`, `v1.0.2-beta.1`, `v1.0.2-beta.2`, `v1.0.2-beta.3`, etc.)**. The `main` branch only contains stable and tested code. **If you are looking for the latest stable version, use the `main` branch.** The `beta` branch might contain experimental features, bugs and should be used with caution.

## ✨ Live Demo

Experience the chatbot in action on Hugging Face Spaces:

[![Try it on Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/DEADS1KE/GASIFHFS)

**Note:** The Hugging Face Space may be running either the `main` or a `beta` version. Check the Space's README for details.

## 🌟 Features

*   **Engaging Conversations:** Chat with Gemini models and experience natural, dynamic conversations.
*   **Text Generation:**  Provide prompts and let Gemini generate creative text formats,  like poems, code, scripts, musical pieces, email, letters, etc.
*   **NEW! Enhanced Image Understanding:** Upload multiple images (JPEG, PNG, GIF, WebP) and ask questions about them.
*   **Customization:**
    *   Adjust the model's temperature and maximum output tokens.
    *   Set a system prompt to guide the chatbot's personality and response style.
*   **Live LaTeX Rendering:** Formulas are rendered in real-time as you type, thanks to the integrated LaTeX support.
*   **Informative Status:** The chatbot displays its current status (e.g., "Sending request...", "Generating response...") and the time it takes to generate responses.
*   **Streamlit-powered UI:** A clean, intuitive interface built with Streamlit.
*   **Open Source:**  The code is open-source and available on GitHub, welcoming contributions.

## 🚀 Getting Started (Local Deployment - `main` branch)

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SparkleSavvy/GASIFHFS.git
    ```

2. **Navigate to the directory:**

    ```bash
    cd GASIFHFS
    ```

3. **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Obtain a Gemini API key:**

    Get your API key from [Google AI Studio](https://ai.google.dev/tutorials/python_quickstart).

6. **Configure the API key (using Streamlit Secrets):**

    *   Go to your Hugging Face Space settings or create `.streamlit/secrets.toml` locally.
    *   Add a secret named `GOOGLE_API_KEY` and paste your API key as the value.

7. **Run the application:**

    ```bash
    streamlit run app.py
    ```

8. **Open in your browser:**
    Access the chatbot at `http://localhost:8501`.

## 🚀 Getting Started (Local Deployment - `beta` branch)

1. **Clone the repository (beta branch):**

    ```bash
    git clone -b beta https://github.com/SparkleSavvy/GASIFHFS.git
    ```

2. **Follow steps 2-8 from the `main` branch instructions.**

**Warning:** The `beta` branch is for development. It might have bugs or incomplete features.

## 🚀 Deploying to Hugging Face Spaces

1. Create a new Space on [Hugging Face Spaces](https://huggingface.co/spaces).
2. Choose "Streamlit" as the SDK.
3. Clone your Space's repository.
4. Copy the files from this repository (either `main` or `beta` branch) to your Space's repository.
5. Add `GOOGLE_API_KEY` as a secret in your Space's settings (Settings -> Repository secrets).
6. Commit and push the changes.

## 📁 File Structure

*   `api.py`: Handles interaction with the Gemini API.
*   `app.py`: Main application code and entry point.
*   `requirements.txt`: Python dependencies.
*   `ui.py`: Streamlit UI components and logic.
*   `utils.py`: Utility functions (e.g., LaTeX rendering, image processing).
*   `README.md`: This file.
*   `SECURITY.md`: Security policy.
*   `LICENSE`: License information.

## 🤝 Contributing

Contributions are welcome!  Please follow these guidelines:

1. **Focus on the `beta` branch:** Active development happens on the `beta` branch.
2. **Create a Pull Request:** Submit your changes as a Pull Request to the `beta` branch.
3. **Clear Description:** Provide a clear description of your changes and why they are needed.

**Note:** The `main` branch is reserved for stable releases.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## ❤️ Author

*   GitHub: [SparkleSavvy](https://github.com/SparkleSavvy)
*   Discord: deads1ke

## 🙏 Acknowledgements

*   [Google AI](https://ai.google.dev/) for the Gemini API.
*   [Hugging Face](https://huggingface.co/) for providing the Spaces platform.
*   [Streamlit](https://streamlit.io/) for the awesome UI framework.

---
---

**Russian**

# 🌠 GASIFHFS - Расширенная версия

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/DEADS1KE/GASIFHFS)
[![GitHub Repo stars](https://img.shields.io/github/stars/SparkleSavvy/GASIFHFS?style=social)](https://github.com/SparkleSavvy/GASIFHFS)

Этот проект с открытым исходным кодом предоставляет удобный интерфейс для взаимодействия с ИИ-моделями Gemini от Google. Исследуйте возможности новейших моделей Gemini в области генерации текста, ведения диалогов и теперь с расширенным пониманием изображений!

> [!TIP]
> Для лучшего отображения формул LaTeX просто установите температуру модели на 0,20 и вставьте этот системный промпт: 
`Вы - могущественный решебник по математике.  Решите следующие задачи, четко показывая свои действия.  Используйте LaTeX для всех математических выражений и уравнений.  Если вы не можете решить задачу, объясните, почему. Проверяйте себя.`

## ❗ Отказ от ответственности

В этом проекте используется **`beta` ветка для активной разработки и предрелизных версий (например, `v1.0.2-alpha.1`, `v1.0.2-alpha.2`, `v1.0.2-beta.1`, `v1.0.2-beta.2`, `v1.0.2-beta.3`, и т.д.)**. Ветка `main` содержит только стабильный и протестированный код. **Если вам нужна последняя стабильная версия, используйте ветку `main`.** Ветка `beta` может содержать экспериментальные функции, ошибки и должна использоваться с осторожностью.

## ✨ Живое демо

Попробуйте чат-бота в действии на Hugging Face Spaces:

[![Try it on Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/DEADS1KE/GASIFHFS)

**Примечание:** На Hugging Face Spaces может быть запущена как `main`, так и `beta` версия. Подробности смотрите в README Spaces.

## 🌟 Возможности

*   **Увлекательные диалоги:** Общайтесь с моделями Gemini и наслаждайтесь естественными и динамичными беседами.
*   **Генерация текста:**  Давайте запросы, и Gemini сгенерирует различные креативные тексты: стихи, код, сценарии, музыкальные произведения, электронные письма, письма и т.д.
*   **НОВОЕ! Расширенное понимание изображений:** Загружайте несколько изображений (JPEG, PNG, GIF, WebP) и задавайте вопросы о них.
*   **Настройка:**
    *   Регулируйте температуру и максимальное количество выходных токенов модели.
    *   Задайте системный промпт, чтобы управлять "личностью" чат-бота и стилем ответа.
*   **Отрисовка LaTeX в реальном времени:** Формулы отображаются по мере ввода благодаря встроенной поддержке LaTeX.
*   **Информативный статус:** Чат-бот отображает свой текущий статус (например, "Отправка запроса...", "Генерация ответа...") и время, затраченное на генерацию ответов.
*   **Пользовательский интерфейс на Streamlit:**  Простой и интуитивно понятный интерфейс, созданный с помощью Streamlit.
*   **Открытый исходный код:** Код открыт и доступен на GitHub, приветствуются улучшения.

## 🚀 Начало работы (Локальное развертывание - ветка `main`)

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/SparkleSavvy/GASIFHFS.git
    ```

2. **Перейдите в директорию:**

    ```bash
    cd GASIFHFS
    ```

3. **Создайте виртуальное окружение (рекомендуется):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

4. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Получите API-ключ Gemini:**

    Получите API-ключ на [Google AI Studio](https://ai.google.dev/tutorials/python_quickstart).

6. **Настройте API-ключ (с помощью Streamlit Secrets):**

    *   Перейдите в настройки вашего Hugging Face Space или создайте `.streamlit/secrets.toml` локально.
    *   Добавьте секрет с именем `GOOGLE_API_KEY` и вставьте ваш API-ключ в качестве значения.

7. **Запустите приложение:**

    ```bash
    streamlit run app.py
    ```

8. **Откройте в браузере:**
    Чат-бот будет доступен по адресу `http://localhost:8501`.

## 🚀 Начало работы (Локальное развертывание - ветка `beta`)

1. **Клонируйте репозиторий (ветка `beta`):**

    ```bash
    git clone -b beta https://github.com/SparkleSavvy/GASIFHFS.git
    ```

2. **Выполните шаги 2-8 из инструкций для ветки `main`.**

**Внимание:** Ветка `beta` предназначена для разработки. Она может содержать ошибки или неполные функции.

## 🚀 Развертывание на Hugging Face Spaces

1. Создайте новое пространство (Space) на [Hugging Face Spaces](https://huggingface.co/spaces).
2. Выберите "Streamlit" в качестве SDK.
3. Клонируйте репозиторий вашего Space.
4. Скопируйте файлы из этого репозитория (ветку `main` или `beta`) в репозиторий вашего Space.
5. Добавьте `GOOGLE_API_KEY` в качестве секрета в настройках вашего Space (Settings -> Repository secrets).
6. Закоммитьте и запушьте изменения.

## 📁 Структура файлов

*   `api.py`: Обработка взаимодействия с API Gemini.
*   `app.py`: Основной код приложения и точка входа.
*   `requirements.txt`: Python-зависимости.
*   `ui.py`: Компоненты и логика пользовательского интерфейса Streamlit.
*   `utils.py`: Вспомогательные функции (например, рендеринг LaTeX, обработка изображений).
*   `README.md`: Этот файл.
*   `SECURITY.md`: Политика безопасности.
*   `LICENSE`: Информация о лицензии.

## 🤝 Участие в проекте

Вклад приветствуется! Пожалуйста, следуйте этим рекомендациям:

1. **Сосредоточьтесь на ветке `beta`:** Активная разработка происходит в ветке `beta`.
2. **Создайте Pull Request:** Отправляйте свои изменения в виде Pull Request в ветку `beta`.
3. **Четкое описание:** Предоставьте четкое описание ваших изменений и зачем они нужны.

**Примечание:** Ветка `main` предназначена для стабильных релизов.

## 📄 Лицензия

Этот проект лицензирован по MIT License - подробности смотрите в файле `LICENSE`.

## ❤️ Автор

*   GitHub: [SparkleSavvy](https://github.com/SparkleSavvy)
*   Discord: deads1ke

## 🙏 Благодарности

*   [Google AI](https://ai.google.dev/) за API Gemini.
*   [Hugging Face](https://huggingface.co/) за предоставление платформы Spaces.
*   [Streamlit](https://streamlit.io/) за потрясающий фреймворк для создания пользовательского интерфейса.
