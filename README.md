# Distributed Task Processing & Workflow Engine

A production-style distributed task processing system built with **FastAPI**, **Redis**, **PostgreSQL**, and a minimal **React** frontend.

Designed to demonstrate real backend engineering fundamentals: asynchronous execution, retries, durability, and observability.

---

## 🚀 Overview

This project implements a **distributed task engine** where:

- Tasks are ingested via a REST API  
- Tasks are queued using Redis  
- Background workers process tasks asynchronously  
- Task state is persisted in PostgreSQL  
- Retries and failures are handled deterministically  
- System-level metrics are exposed  
- A minimal React frontend demonstrates end-to-end behavior  

This is **not a demo app**. It is a simplified representation of patterns used in real production systems.

---

## 🧠 Key Features

- Asynchronous task processing  
- Redis-backed task queue  
- PostgreSQL as the source of truth  
- Retry logic with failure caps  
- Task status tracking  
- System metrics (success and failure rates)  
- Decoupled background worker  
- Minimal frontend for observability  

---

## 🏗 Architecture

### High-Level Flow

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


### Component Interaction

```mermaid
graph TD
    A[React Client] -->|Create Task| B[FastAPI API]
    B -->|Persist Task| C[PostgreSQL]
    B -->|Enqueue Task| D[Redis Queue]
    D -->|Consume| E[Worker Process]
    E -->|Update Status| C
    B -->|Expose Metrics| A
```
🛠 Tech Stack
Backend

Python 3.11+

FastAPI

Redis

PostgreSQL

SQLAlchemy

Uvicorn

Frontend

React (Vite)

Fetch API

Minimal CSS

Infrastructure

Environment-based configuration

Background worker model

CORS-enabled API

📂 Project Structure

task-engine/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── api.py           # API routes
│   ├── worker.py        # Background worker
│   ├── queue.py         # Redis queue logic
│   ├── models.py        # Database models
│   ├── database.py      # DB connection
│   └── config.py        # Environment config
│
├── frontend/            # React UI
│
├── tests/
├── requirements.txt
├── README.md
├── .env.example


▶️ How to Run Locally
1. Clone the repository

git clone https://github.com/anujmundu/Distributed-Task-Processing-Workflow-Engine.git
cd Distributed-Task-Processing-Workflow-Engine

2. Backend setup

python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt

Create a .env file:
REDIS_URL=redis://localhost:6379
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb

Run the API:

uvicorn app.main:app --reload


Run the worker (separate terminal):

python -m app.worker

3. Frontend setup
cd frontend
npm install
npm run dev


Frontend:

http://localhost:5173


Backend:

http://127.0.0.1:8000

🔍 API Endpoints

POST /tasks – Create a task

GET /tasks/{task_id} – Retrieve task status

GET /metrics – System metrics

Swagger UI:

http://127.0.0.1:8000/docs

📊 Metrics Example
{
  "total_tasks": 22,
  "completed": 9,
  "failed": 0,
  "success_rate": 0.41,
  "failure_rate": 0
}

🎯 Why This Project

This project demonstrates:

Backend system design

Asynchronous processing patterns

Separation of concerns

Reliability under failure

Production-ready structure

It was built to be interview-defensible, not tutorial-driven.

👤 Author

Anuj Mundu
MCA Student | Backend & Full-Stack Developer

GitHub: https://github.com/anujmundu

LinkedIn: https://www.linkedin.com/in/anujmundu/

📧 Contact: anujmark.edwin.ame@gmail.com