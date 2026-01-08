# Distributed Task Processing & Workflow Engine

A production-style distributed task processing system built with FastAPI, Redis, PostgreSQL, and a minimal React frontend.  
Designed to demonstrate real backend engineering fundamentals: async execution, retries, durability, and observability.

---

## 🚀 Overview

This project implements a **distributed task engine** where:

- Tasks are ingested via a REST API
- Tasks are queued in Redis
- Background workers process tasks asynchronously
- Task state is persisted in PostgreSQL
- Retries and failures are handled deterministically
- System metrics are exposed
- A minimal React frontend demonstrates end-to-end behavior

This is **not a demo app**. It is a simplified version of systems used in real production environments.

---

## 🧠 Key Features

- **Asynchronous task processing**
- **Redis-backed task queue**
- **PostgreSQL as source of truth**
- **Retry logic with failure caps**
- **Task status tracking**
- **System metrics (success/failure rates)**
- **Decoupled worker process**
- **Minimal frontend for observability**

---

## 🏗 Architecture


```mermaid
graph TD
    A[FastAPI REST API] -->|Task Submission| B[Redis Queue]
    B -->|Task Processing| C[Background Worker]
    C -->|State Updates| D[PostgreSQL]
    D -->|Task Status| E[React Frontend]
    E -->|Metrics| A

Client (React)
|
v
FastAPI (API Layer)
|
v
PostgreSQL (Durable State)
|
v
Redis (Task Queue)
|
v
Worker Process (Task Execution)
```


---

## 🛠 Tech Stack

### Backend
- Python 3.11+
- FastAPI
- Redis
- PostgreSQL
- SQLAlchemy
- Uvicorn

### Frontend
- React (Vite)
- Fetch API
- Minimal CSS

### Infrastructure
- Environment-based configuration
- Background worker model
- CORS-enabled API

---

## 📂 Project Structure


```
task-engine/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── api.py # API routes
│ ├── worker.py # Background worker
│ ├── queue.py # Redis queue logic
│ ├── models.py # Database models
│ ├── database.py # DB connection
│ └── config.py # Environment config
│
├── frontend/ # React UI
│
├── tests/
├── requirements.txt
├── README.md
├── .env.example
```

---

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/anujmundu/Distributed-Task-Processing-Workflow-Engine.git
cd Distributed-Task-Processing-Workflow-Engine
```
### 2. Backend setup
```
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

```

### Configure .env:
```
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
```
### Run API:
```
uvicorn app.main:app --reload
```

### Run worker (separate terminal):
```
python -m app.worker
```

### 3. Frontend setup

cd frontend
npm install
npm run dev


### Frontend runs at:

http://localhost:5173


### Backend runs at:

http://127.0.0.1:8000

### API Endpoints

POST /tasks – Create a task

GET /tasks/{task_id} – Get task status

GET /metrics – System metrics

Swagger UI:
```
http://127.0.0.1:8000/docs
```

### Metrics Example
{
  "total_tasks": 22,
  "completed": 9,
  "failed": 0,
  "success_rate": 0.41,
  "failure_rate": 0
}

### 🎯 Why This Project

This project demonstrates:

Backend system design

Async processing patterns

Separation of concerns

Reliability under failure

Production-ready structure

It was built to be interview-defensible, not tutorial-driven.


---

👤 Author

Anuj Mundu
MCA Student | Backend & Full-Stack Developer
GitHub: https://github.com/anujmundu
LinkedIn: https://www.linkedin.com/in/anujmundu/
