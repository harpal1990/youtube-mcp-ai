# 🎥 YouTube MCP Server – AI-Powered YouTube Video Reader

## 🚀 Project Overview

YouTube MCP Server is an AI-powered application that can:

- Read YouTube video transcripts
- Generate AI summaries
- Answer questions from videos
- Act as an MCP-style AI tool server
- Provide a Web Console UI
- Run fully locally using Ollama

This project is ideal for:

- AI Engineers
- DevOps Engineers
- MCP Developers
- Ollama Users
- FastAPI Developers
- YouTube Content Creators

---

# 🏗️ Architecture

## High-Level Flow

```text
User Browser
     ↓
Frontend Web Console
     ↓
FastAPI Backend (MCP Server)
     ↓
YouTube Transcript API
     ↓
Ollama Local AI Model
     ↓
AI Summary / AI Answers
```

---

# 📁 Project Structure

```bash
youtube-mcp-server/
│
├── app.py
├── requirements.txt
├── README.md
│
├── tools/
│   ├── __init__.py
│   ├── transcript.py
│   ├── summarize.py
│   └── qa.py
│
├── utils/
│   ├── __init__.py
│   └── youtube.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── app.js
│
└── venv/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/harpal1990/youtube-mcp-ai.git
cd youtube-mcp-ai
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

```txt
fastapi
uvicorn
jinja2
python-multipart
youtube-transcript-api
ollama
```

---

# 🧠 Install Ollama

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Pull Lightweight AI Model

```bash
ollama pull phi3
```

---

## Start Ollama

```bash
ollama run phi3
```

---

# ▶️ Run Application

```bash
uvicorn app:app --reload
```

---

# 🌐 Access Web Console

```text
http://127.0.0.1:8000
```

---

# ✨ Features

## ✅ Get Transcript
Fetches complete transcript from YouTube video.

---

## ✅ AI Summary
Generates lightweight AI summary using Ollama.

---

## ✅ Ask Questions
Ask questions directly from YouTube videos.

Example:

```text
What AWS services are used?
```

---

# 🔥 API Endpoints

## Get Transcript

```http
POST /get_transcript
```

---

## Summarize Video

```http
POST /summarize
```

---

## Ask Questions

```http
POST /ask
```

---

# 🚀 Future Enhancements

- Telegram Bot Integration
- Multi-video comparison
- PDF export
- AWS integration
- Voice output
- YouTube playlist analysis
- ChatGPT-style conversation memory

---

# 🧪 Example Use Cases

## 📚 Learn Faster
Summarize long tutorials instantly.

---

## ☁️ DevOps Learning
Extract AWS/Kubernetes commands from videos.

---

## 🎓 Student Notes
Convert lectures into short notes.

---

# 🛠️ Tech Stack

- Python
- FastAPI
- Ollama
- phi3
- YouTube Transcript API
- HTML/CSS/JavaScript

---
