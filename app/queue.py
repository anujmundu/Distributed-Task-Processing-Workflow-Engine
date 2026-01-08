import redis
import json
import uuid
from app.config import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL)

QUEUE_NAME = "task_queue"

def enqueue_task(task_type: str, payload: dict) -> str:
    task_id = str(uuid.uuid4())

    task_data = {
        "id": task_id,
        "type": task_type,
        "payload": payload
    }

    redis_client.lpush(QUEUE_NAME, json.dumps(task_data))
    return task_id
