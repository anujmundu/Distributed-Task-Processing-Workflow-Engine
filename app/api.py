from fastapi import APIRouter, HTTPException
from app.queue import enqueue_task
from app.database import SessionLocal
from app.models import Task

router = APIRouter()

@router.post("/tasks")
def create_task(task_type: str, payload: dict):
    db = SessionLocal()

    task_id = enqueue_task(task_type, payload)

    task = Task(
        id=task_id,
        status="queued",
        attempts=0,
        payload=payload
    )

    db.add(task)
    db.commit()
    db.close()

    return {
        "task_id": task_id,
        "status": "queued"
    }

@router.get("/tasks/{task_id}")
def get_task(task_id: str):
    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return {
            "id": task.id,
            "status": task.status,
            "attempts": task.attempts,
            "result": task.result,
        }
    finally:
        db.close()

@router.get("/metrics")
def metrics():
    db = SessionLocal()
    try:
        total = db.query(Task).count()
        completed = db.query(Task).filter(Task.status == "completed").count()
        failed = db.query(Task).filter(Task.status == "failed").count()

        return {
            "total_tasks": total,
            "completed": completed,
            "failed": failed,
            "success_rate": completed / total if total else 0,
            "failure_rate": failed / total if total else 0,
        }
    finally:
        db.close()
