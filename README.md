# Gemini Chatbot - Hugging Face Space

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME)

This repository contains the source code for a chatbot deployed on Hugging Face Spaces that utilizes the Google Gemini API for generating responses.

## Description

This chatbot allows you to interact with Google AI's Gemini Pro model through a simple web interface. It can answer your questions, engage in conversations, and generate text based on your prompts.

## How to Use

1. **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    ```

2. **Navigate to the repository directory:**

    ```bash
    cd YOUR_REPOSITORY_NAME
    ```

3. **Create and activate a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows
    ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Obtain a Gemini API key:**

    Follow the instructions on the [Google AI Studio](https://ai.google.dev/tutorials/python_quickstart) website to get your API key.

6. **Configure the API key:**

    *   **Option 1 (Environment Variable):** Set an environment variable named `GOOGLE_API_KEY` with your API key as the value.
        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"  # For Linux/macOS
        set GOOGLE_API_KEY="YOUR_API_KEY"  # For Windows
        ```
    *   **Option 2 (In Code):** Replace `gr.Secret.from_name("GOOGLE_API_KEY")` or `st.secrets["GOOGLE_API_KEY"]` in the `app.py` file with your API key `"<YOUR_API_KEY>"` - **not recommended for public repositories**.

7. **Run the application:**

    *   **If you used Gradio:**
        ```bash
        python app.py
        ```
    *   **If you used Streamlit:**
        ```bash
        streamlit run app.py
        ```

8. **Open the application in your browser:**
    The application will be available at `http://localhost:7860` (Gradio) or `http://localhost:8501` (Streamlit).

## Deploying to Hugging Face Spaces

1. Create a new Space on [Hugging Face Spaces](https://huggingface.co/spaces).
2. Choose "Gradio" or "Streamlit" as the SDK.
3. Clone the repository of your Space.
4. Copy the files from this repository to your Space's repository.
5. Add `GOOGLE_API_KEY` as a secret in your Space's settings (Settings -> Repository secrets).
6. Commit and push the changes to the Space repository.

## File Structure

*   `app.py`: The main file containing the application code.
*   `requirements.txt`: The list of Python dependencies.
*   `README.md`: This file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. (Remember to add a `LICENSE` file with the MIT license text to the root of your repository.)

## Author

YOUR NAME (YOUR_CONTACT)

## Acknowledgements

*   [Google AI](https://ai.google.dev/) for the Gemini API.
*   [Hugging Face](https://huggingface.co/) for the Spaces platform.
*   [Gradio](https://gradio.app/) / [Streamlit](https://streamlit.io/) for the user-friendly web interface libraries.

## Contributing

If you'd like to contribute to this project, please create a Pull Request.

---
