const BASE_URL = "http://127.0.0.1:8000";

export async function createTask(payload) {
  const res = await fetch(`${BASE_URL}/tasks?task_type=email`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}

export async function getTask(taskId) {
  const res = await fetch(`${BASE_URL}/tasks/${taskId}`);
  return res.json();
}

export async function getMetrics() {
  const res = await fetch(`${BASE_URL}/metrics`);
  return res.json();
}
