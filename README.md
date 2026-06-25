#   AI Mentor Chatbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/Mistral_7B-7B2D8B?style=for-the-badge&logo=ai&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenRouter-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  An AI-powered career mentor chatbot built with <b>Streamlit, LangChain & Mistral-7B via OpenRouter</b> — providing career guidance, course suggestions, and resume-building advice.
</p>

---

##  Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Setup & Installation](#-setup--installation)
- [Configuration](#-configuration)
- [How It Works](#-how-it-works)
- [Author](#-author)

---

## Overview

**Cognitia** is an AI-powered career mentoring chatbot designed to guide students and professionals in the field of Artificial Intelligence. It leverages **Mistral-7B Instruct** via **OpenRouter** and **LangChain** to deliver context-aware, conversational career advice — all wrapped in a clean **Streamlit** interface.

---

## Features

| Feature | Description |
|:---|:---|
|  Career Guidance | Personalized advice on career paths in AI & tech |
|  Course Suggestions | Recommends relevant courses and learning resources |
|  Resume Tips | Offers professional resume-building advice |
|  Multi-turn Chat | Maintains full conversation history per session |
|  Safe Responses | Steers away from harmful or off-topic content |
|  Fast Responses | Powered by Mistral-7B Instruct via OpenRouter |

---

##  Tech Stack

| Tool | Purpose |
|:---|:---|
| Python | Core language |
| Streamlit | Web UI & app framework |
| streamlit-chat | Chat message UI components |
| LangChain | LLM orchestration & message handling |
| Mistral-7B Instruct | Underlying language model |
| OpenRouter | LLM API gateway |
| python-dotenv | Environment variable management |

---

##  Project Structure

```
cognitia/
│
├──  cognitia_consolidated.py      # Main application file
├──  requirements.txt              # Python dependencies
├──  README.md                     # Project documentation
└──  .streamlit/
    └── secrets.toml                 # API keys (do NOT commit this)
```

---

##  Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/cognitia-ai-mentor.git
cd cognitia-ai-mentor
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit streamlit-chat python-dotenv langchain langchain-openai openai
```

**3. Configure API keys** *(see below)*

**4. Run the app**

```bash
streamlit run cognitia_consolidated.py
```

---

##  Configuration

Create a `.streamlit/secrets.toml` file in the project root:

```toml
OPENROUTER_API_KEY = "your-openrouter-api-key-here"
OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
```

>  **Never commit `secrets.toml` to GitHub.** Add it to `.gitignore`:

```bash
echo ".streamlit/secrets.toml" >> .gitignore
```

Get your free API key at  [openrouter.ai](https://openrouter.ai)

---

##  Components

| Component | Role |
|:---|:---|
| `build_message_list()` | Constructs full chat history with system prompt |
| `generate_response()` | Sends messages to LLM and returns AI reply |
| `submit()` | Handles input field state on form submission |
| `SystemMessage` | Defines Cognitia's persona and behavior rules |
| Session State | Stores `past` (user) and `generated` (AI) messages |

**System Prompt Behavior:**
-  Greets users politely
-  Provides career & AI-related guidance only
-  Keeps responses under 100 words
-  Avoids harmful or off-topic content
-  Ends conversations gracefully

---

## Author

**Sadia Noreen**
*Software Engineering Graduate | AI & ML Enthusiast*

---

<p align="center"> If you found this helpful, consider giving it a star!</p>
