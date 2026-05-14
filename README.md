# AI DevOps Monitoring Platform 🚀

Professional AI-powered DevOps Monitoring Backend using FastAPI, Docker, Git, and GitHub.

---

# Features 🔥

- FastAPI Backend
- Docker Containerization
- System Monitoring APIs
- CPU Usage Monitoring
- Memory Usage Monitoring
- Health Check APIs

---

# Tech Stack 🛠️

| Technology | Usage |
|---|---|
| Python | Backend Language |
| FastAPI | API Framework |
| Docker | Containerization |
| Git | Version Control |
| GitHub | Remote Repository |
| Uvicorn | ASGI Server |

---

# API Endpoints 📡

| Endpoint | Description |
|---|---|
| / | Home API |
| /health | Health Check |
| /system-info | System Information |
| /cpu | CPU Usage |
| /memory | Memory Usage |
| /hostname | Hostname Info |

---

# Run Locally 💻

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

# Docker Run 🐳

```bash
docker build -t ai-devops-monitor .
docker run -d -p 8000:8000 --name ai-monitor-container ai-devops-monitor
```

---

# API Documentation 📄

```text
http://localhost:8000/docs
```

---

# Author 😎

RahulPlatform0210
