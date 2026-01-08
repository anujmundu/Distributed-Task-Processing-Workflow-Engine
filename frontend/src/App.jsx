import { useState } from "react";
import TaskForm from "./components/TaskForm";
import TaskStatus from "./components/TaskStatus";
import Metrics from "./components/Metrics";

export default function App() {
  const [taskId, setTaskId] = useState(null);

  return (
    <div style={{ maxWidth: 600, margin: "40px auto", fontFamily: "sans-serif" }}>
      <h2>Distributed Task Engine</h2>

      <TaskForm onTaskCreated={setTaskId} />

      <hr />

      <TaskStatus taskId={taskId} />

      <hr />

      <Metrics />
    </div>
  );
}
