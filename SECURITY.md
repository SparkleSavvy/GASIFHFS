# Security Policy

## Supported Versions

This project uses two main branches: `main` and `beta`.

*   **`main`:** This branch represents the latest stable version of the project and is actively supported.
*   **`beta`:** This branch is used for development and testing of new features, including pre-release versions (e.g., `v1.0.2-alpha.1`, `v1.0.2-alpha.2`, `v1.0.2-beta.1` etc.). **The `beta` branch, and any versions derived from it, are not officially supported and may contain unstable or experimental code.**

**Security updates will only be applied to the `main` branch.**

| Branch  | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| beta    | :x:                |

## Reporting a Vulnerability

We take the security of our project seriously. If you believe you have found a security vulnerability, **please report it only if it affects the `main` branch**. Vulnerabilities found in the `beta` branch should be reported as regular issues.

**How to Report (for `main` branch vulnerabilities):**

1. **DO NOT CREATE A PUBLIC ISSUE FOR POTENTIAL SECURITY VULNERABILITIES.**
2. **Contact us privately through one of the following methods:**
    *   **Discord:** `deads1ke`
    *   **Email:** `bafef.one@gmail.com`

3. **Provide a detailed description of the vulnerability.** Please include as much of the following information as possible:
    *   **Type of vulnerability** (e.g., "Possible XSS", "Potential data leak").
    *   **Full paths of the source file(s) related to the manifestation of the vulnerability.**
    *   **The location of the affected source code** (commit or direct URL). **Please specify that the issue is present on the `main` branch.**
    *   **Step-by-step instructions to reproduce the issue.**
    *   **Proof-of-concept or exploit code (if available).**
    *   **The potential impact of the vulnerability.**
    *   **Any special configuration required to reproduce the issue.**

**What to Expect:**

*   We will acknowledge receipt of your vulnerability report as soon as possible, usually within 48 hours.
*   We will investigate the report and work on a fix if the vulnerability is confirmed.
*   We will keep you informed of our progress in resolving the vulnerability.
*   Once a fix is ready, we will release it as soon as possible, depending on the complexity and severity.
*   We will publicly acknowledge your contribution to the release notes unless you prefer to remain anonymous.

**Please Note:**

*   This project relies on the Google Gemini API. Vulnerabilities in the API itself are outside the scope of this project and should be reported to Google directly.
*   We are a small team/individual developer, and our response times may vary.
*   **Disclosing vulnerability details publicly before we have a chance to address them puts all users at risk. Please be responsible and allow us time to investigate and develop a fix.**
*   **Vulnerabilities found on the `beta` branch should be reported as regular issues, not through the security vulnerability reporting process.**

We appreciate your help in keeping the Gemini API Chatbot and its users safe!

---
---

# Политика безопасности

## Поддерживаемые версии

В этом проекте используются две основные ветки: `main` и `beta`.

*   **`main`:** Эта ветка представляет последнюю стабильную версию проекта и активно поддерживается.
*   **`beta`:** Эта ветка используется для разработки и тестирования новых функций, включая предварительные версии (например, `v1.0.2-alpha.1`, `v1.0.2-alpha.2`, `v1.0.2-beta.1` и т.д.). **Ветка `beta` и любые производные от нее версии официально не поддерживаются и могут содержать нестабильный или экспериментальный код.**

**Обновления безопасности будут применяться только к ветке `main`.**

| Ветка   | Поддерживается     |
| ------- | ------------------ |
| main    | :white_check_mark: |
| beta    | :x:                |

## Сообщение об уязвимости

Мы серьезно относимся к безопасности нашего проекта. Если вы считаете, что обнаружили уязвимость безопасности, **пожалуйста, сообщайте о ней только в том случае, если она затрагивает ветку `main`**. Об уязвимостях, обнаруженных в ветке `beta`, следует сообщать как об обычных проблемах.

**Как сообщить (об уязвимостях в ветке `main`):**

1. **НЕ СОЗДАВАЙТЕ ПУБЛИЧНЫЙ ISSUE ДЛЯ ПОТЕНЦИАЛЬНЫХ УЯЗВИМОСТЕЙ БЕЗОПАСНОСТИ.**
2. **Свяжитесь с нами конфиденциально через один из следующих методов:**
    *   **Discord:** `deads1ke`
    *   **Email:** `bafef.one@gmail.com`

3. **Предоставьте подробное описание уязвимости.** Пожалуйста, включите как можно больше следующей информации:
    *   **Тип уязвимости** (например, "Возможная XSS", "Потенциальная утечка данных").
    *   **Полные пути к исходным файлам, связанным с проявлением уязвимости.**
    *   **Местоположение затронутого исходного кода** (коммит или прямой URL). **Пожалуйста, укажите, что проблема присутствует в ветке `main`.**
    *   **Пошаговые инструкции для воспроизведения проблемы.**
    *   **Код, подтверждающий концепцию, или эксплойт (если есть).**
    *   **Потенциальное влияние уязвимости.**
    *   **Любая специальная конфигурация, необходимая для воспроизведения проблемы.**

**Что ожидать:**

*   Мы подтвердим получение вашего сообщения об уязвимости как можно скорее, обычно в течение 48 часов.
*   Мы расследуем отчет и разработаем исправление, если уязвимость подтвердится.
*   Мы будем держать вас в курсе нашего прогресса в устранении уязвимости.
*   Как только исправление будет готово, мы выпустим его как можно скорее, в зависимости от сложности и серьезности.
*   Мы публично отметим ваш вклад в примечаниях к выпуску, если вы не предпочтете остаться анонимным.

**Пожалуйста, примите во внимание:**

*   Этот проект использует Google Gemini API. Уязвимости в самом API находятся вне зоны ответственности этого проекта, и о них следует сообщать непосредственно в Google.
*   Мы - небольшая команда/индивидуальный разработчик, и время нашего ответа может варьироваться.
*   **Публичное раскрытие деталей уязвимости до того, как у нас будет возможность их устранить, подвергает риску всех пользователей. Пожалуйста, будьте ответственны и дайте нам время на расследование и разработку исправления.**
*   **Об уязвимостях, обнаруженных в ветке `beta`, следует сообщать как об обычных проблемах, а не через процесс сообщения об уязвимостях безопасности.**

Мы ценим вашу помощь в обеспечении безопасности чат-бота Gemini API и его пользователей!
