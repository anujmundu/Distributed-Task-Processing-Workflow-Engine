import { useEffect, useState } from "react";
import { getTask } from "../api";

export default function TaskStatus({ taskId }) {
  const [task, setTask] = useState(null);

  useEffect(() => {
    if (!taskId) return;

    const interval = setInterval(async () => {
      const data = await getTask(taskId);
      setTask(data);
    }, 2000);

    return () => clearInterval(interval);
  }, [taskId]);

  if (!task) return null;

  return (
    <div>
      <h3>Task Status</h3>
      <p><b>Status:</b> {task.status}</p>
      <p><b>Attempts:</b> {task.attempts}</p>
      <pre>{JSON.stringify(task.result, null, 2)}</pre>
    </div>
  );
}
