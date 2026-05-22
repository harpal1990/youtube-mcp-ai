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
git clone https://github.com/yourusername/youtube-mcp-server.git
cd youtube-mcp-server
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

# 🎥 YouTube Video Script

# 🎬 INTRO (0:00 - 0:30)

“Imagine an AI that watches YouTube videos for you.

You paste a YouTube link.

It reads the transcript.

Summarizes the content.

And even answers your questions.

Today we are building a complete YouTube MCP Server using FastAPI + Ollama + AI.”

---

# 🧠 WHAT IS MCP? (0:30 - 1:30)

“MCP stands for Model Context Protocol.

It allows AI models to connect with external tools.

In this project:

AI → MCP Server → YouTube Data

This creates a powerful AI workflow.”

---

# ⚙️ PROJECT DEMO (1:30 - 4:00)

- Open Web Console
- Paste YouTube URL
- Click Summarize
- Show AI Summary
- Ask AI question from video
- Show transcript feature

Example:

“What AWS services are explained in this video?”

---

# 🔥 CODE WALKTHROUGH (4:00 - 8:00)

Explain:

- FastAPI backend
- Transcript extraction
- Ollama integration
- Frontend JavaScript
- API endpoints

---

# 🚀 FUTURE IDEAS (8:00 - 9:00)

- Telegram bot
- AWS automation
- Multi-video analysis
- AI note generation

---

# 🎯 OUTRO (9:00 - END)

“If you enjoyed this AI + MCP project,

Like the video,
Subscribe to TechServerGlobal,

And I’ll create more advanced MCP + AI automation projects.”

---

# 🏆 Suggested YouTube Titles

## 🔥 Best Titles

1. Build AI That Watches YouTube Videos | MCP + Ollama + FastAPI
2. Create Your Own YouTube AI Assistant (Full MCP Project)
3. AI Reads YouTube Videos for You 🤯 | FastAPI + Ollama
4. Build a YouTube MCP Server Using Python
5. AI YouTube Summarizer with Ollama and MCP

---

# 🎨 Thumbnail Text Ideas

## Thumbnail Option 1

```text
AI WATCHES
YOUTUBE 😳
```

---

## Thumbnail Option 2

```text
BUILD YOUR OWN
YOUTUBE AI
```

---

## Thumbnail Option 3

```text
MCP + AI + YOUTUBE
FULL PROJECT
```

---

# 🎯 Recommended Thumbnail Style

- Dark futuristic background
- YouTube logo
- AI robot face
- FastAPI logo
- Ollama logo
- Glowing neon elements
- Your photo pointing toward AI dashboard

---

# 📢 Recommended GitHub Repo Name

```text
youtube-mcp-server
```

Alternative:

```text
ai-youtube-reader
```

---

# 🏷️ Recommended Tags

```text
mcp
ollama
fastapi
ai agent
python ai
youtube ai
ollama tutorial
mcp server
ai automation
local llm
```

---

# 📣 YouTube Description

Build a complete AI-powered YouTube MCP Server using Python, FastAPI, Ollama, and local AI models.

This project can:
- Read YouTube transcripts
- Summarize videos
- Answer questions from videos
- Run locally using Ollama
- Provide a web-based MCP client dashboard

Perfect for AI engineers, DevOps engineers, and MCP developers.

GitHub Repo:
https://github.com/yourusername/youtube-mcp-server

#AI #MCP #Ollama #FastAPI #Python

