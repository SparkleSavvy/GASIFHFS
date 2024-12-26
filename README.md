# 🌠 Gemini Chatbot - Hugging Face Space

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/DEADS1KE/Gemeni-Exp-1206)

This repository contains the source code for a chatbot deployed on Hugging Face Spaces that utilizes the Google Gemini API for generating responses.

## ❗ Disclaimer

This project now uses a **`beta` branch for active development and pre-release versions (e.g., `alpha.1`, `alpha.2`, etc.)**. The `main` branch only contains stable and tested code. **If you are looking for the latest stable version, use the `main` branch.** The `beta` branch might contain experimental features, bugs and should be used with caution.

## Description

This chatbot allows you to interact with Google AI's Gemini models through a simple web interface. It can answer your questions, engage in conversations, generate text based on your prompts and process images.

## ✨ Try it out!

You can try out the chatbot directly on Hugging Face Spaces by clicking the button below:

[![Try it on Hugging Face Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm.svg)](https://huggingface.co/spaces/DEADS1KE/Gemeni-Exp-1206)

**Note:** The Hugging Face Space may be running either the `main` or a `beta` version. Check the Space's README for details.

## How to Use (Locally - `main` branch)

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SparkleSavvy/GASIFHFS.git
    ```

2. **Navigate to the repository directory:**

    ```bash
    cd GASIFHFS
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

6. **Configure the API key (using Streamlit Secrets):**

    *   Go to your Hugging Face Space settings.
    *   Navigate to "Repository secrets".
    *   Add a new secret named `GOOGLE_API_KEY` and paste your API key as the value.

7. **Run the application:**

    ```bash
    streamlit run app.py
    ```

8. **Open the application in your browser:**
    The application will be available at `http://localhost:8501`.

## How to Use (Locally - `beta` branch)

1. **Clone the repository:**

    ```bash
    git clone -b beta https://github.com/SparkleSavvy/GASIFHFS.git
    ```
    **Note:** The `-b beta` part specifies that you want to clone the `beta` branch.

2. **Follow steps 2-8 from the `main` branch instructions.** The process is the same, but you will be working with the `beta` code.

**Warning:** The `beta` branch is for development purposes. It might contain bugs or incomplete features.

## Deploying to Hugging Face Spaces

1. Create a new Space on [Hugging Face Spaces](https://huggingface.co/spaces).
2. Choose "Streamlit" as the SDK.
3. Clone the repository of your Space.
4. Copy the files from this repository to your Space's repository. **Make sure to copy the desired branch (`main` or `beta`).**
5. Add `GOOGLE_API_KEY` as a secret in your Space's settings (Settings -> Repository secrets).
6. Commit and push the changes to the Space repository.

## File Structure

*   `app.py`: The main file containing the application code.
*   `requirements.txt`: The list of Python dependencies.
*   `README.md`: This file.
*   `SECURITY.md`: The security policy.
*   `LICENSE`: The license file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## ❤️ Author

*   GitHub: [SparkleSavvy](https://github.com/SparkleSavvy)
*   Discord: deads1ke

## Acknowledgements

*   [Google AI](https://ai.google.dev/) for the Gemini API.
*   [Hugging Face](https://huggingface.co/) for the Spaces platform.
*   [Streamlit](https://streamlit.io/) for the user-friendly web interface library.

## Contributing

If you'd like to contribute to this project, please first check the `beta` branch, as that's where active development takes place. Create a Pull Request to the `beta` branch with your changes.

**Please Note:** The `main` branch is reserved for stable releases.
