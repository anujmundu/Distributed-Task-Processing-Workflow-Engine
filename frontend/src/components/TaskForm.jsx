import { useState } from "react";
import { createTask } from "../api";

export default function TaskForm({ onTaskCreated }) {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit() {
    if (!message) return;

    setLoading(true);
    const task = await createTask({
      to: "frontend@example.com",
      message,
    });
    setLoading(false);
    setMessage("");
    onTaskCreated(task.task_id);
  }

  return (
    <div>
      <h3>Create Task</h3>
      <input
        placeholder="Task message"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={submit} disabled={loading}>
        {loading ? "Submitting..." : "Submit"}
      </button>
    </div>
  );
}
