# Smart AI Study Assistant

A simple web application where students can **ask questions**, **summarize notes**, and **generate quizzes** using AI. Built with Python and Streamlit.

## Features

- **Ask AI** — Type any study question and get a clear explanation.
- **Summarize Notes** — Paste long notes and get a short bullet-point summary.
- **Generate Quiz** — Enter a topic and get 5 quiz questions with answers.

## Prerequisites

- Python 3.8 or higher
- An API key from either:
  - [OpenAI](https://platform.openai.com/api-keys) (for GPT), or
  - [Google AI Studio](https://aistudio.google.com/apikey) (for Gemini)

## Installation

### 1. Clone or download this project

```bash
cd ai-study-assistant
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Adding Your API Key

Use **one** of the following methods.

### Option A: Environment variable (recommended)

- **Windows (PowerShell):**
  ```powershell
  $env:OPENAI_API_KEY = "your-openai-key-here"
  # OR
  $env:GEMINI_API_KEY = "your-gemini-key-here"
  ```

- **macOS/Linux:**
  ```bash
  export OPENAI_API_KEY="your-openai-key-here"
  # OR
  export GEMINI_API_KEY="your-gemini-key-here"
  ```

### Option B: `.env` file in the project folder

1. Create a file named `.env` in the same folder as `app.py`.
2. Add one line (use either OpenAI or Gemini, not both required):

   ```
   OPENAI_API_KEY=your-openai-key-here
   ```
   or
   ```
   GEMINI_API_KEY=your-gemini-key-here
   ```

3. Do not commit `.env` to git (it should be in `.gitignore`).

The app will use **OpenAI** if `OPENAI_API_KEY` is set, otherwise **Gemini** if `GEMINI_API_KEY` is set.

## How to Run the App

From the project folder (with your virtual environment activated):

```bash
streamlit run app.py
```

Your browser will open to a local URL (usually `http://localhost:8501`). Use the sidebar to switch between **Ask AI**, **Summarize Notes**, and **Generate Quiz**.

## Project Structure

```
ai-study-assistant/
├── app.py           # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md        # This file
└── .env             # Your API key (create this yourself, do not commit)
```

## License

This project is for educational use. Respect your API provider’s terms of use (OpenAI or Google).
