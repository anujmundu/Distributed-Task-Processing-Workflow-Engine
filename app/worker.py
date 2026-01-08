import json
import time
import redis
from sqlalchemy.orm import Session

from app.config import REDIS_URL
from app.database import SessionLocal
from app.models import Task

MAX_RETRIES = 3

QUEUE_NAME = "task_queue"

redis_client = redis.Redis.from_url(REDIS_URL)


import random

def process_task(task_data: dict) -> dict:
    time.sleep(2)
    return {"message": f"Processed task of type {task_data['type']}"}



def handle_task(task_data: dict):
    db: Session = SessionLocal()
    task_id = task_data["id"]

    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return

        # if already completed or permanently failed, ignore
        if task.status in ("completed", "failed"):
            return

        task.status = "processing"
        task.attempts += 1
        db.commit()

        result = process_task(task_data)

        task.status = "completed"
        task.result = result
        db.commit()

    except Exception as e:
        if task.attempts >= MAX_RETRIES:
            task.status = "failed"
            task.result = {"error": str(e)}
            db.commit()
        else:
            task.status = "queued"
            db.commit()

            # requeue task
            redis_client.lpush(QUEUE_NAME, json.dumps(task_data))

    finally:
        db.close()


def worker_loop():
    print("Worker started. Waiting for tasks...")

    while True:
        print("Blocking on Redis BRPOP...")
        _, raw_task = redis_client.brpop(QUEUE_NAME)
        print("Raw task received:", raw_task)

        task_data = json.loads(raw_task)
        print("Parsed task:", task_data)

        handle_task(task_data)
        print("Task handled:", task_data["id"])



if __name__ == "__main__":
    worker_loop()
