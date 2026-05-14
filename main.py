from fastapi import FastAPI
import platform
import psutil
import socket
from datetime import datetime

app = FastAPI(
    title="AI DevOps Monitoring API",
    description="Professional Monitoring Backend for DevOps Project",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI DevOps Monitoring API Running 🚀"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now()
    }

@app.get("/system-info")
def system_info():
    return {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "processor": platform.processor()
    }

@app.get("/cpu")
def cpu_usage():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1)
    }

@app.get("/memory")
def memory_usage():
    memory = psutil.virtual_memory()

    return {
        "total_memory": memory.total,
        "used_memory": memory.used,
        "memory_percent": memory.percent
    }

@app.get("/hostname")
def hostname():
    return {
        "hostname": socket.gethostname()
    }

