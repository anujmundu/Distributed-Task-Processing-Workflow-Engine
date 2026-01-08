import { useEffect, useState } from "react";
import { getMetrics } from "../api";

export default function Metrics() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    async function load() {
      setMetrics(await getMetrics());
    }
    load();
  }, []);

  if (!metrics) return null;

  return (
    <div>
      <h3>System Metrics</h3>
      <pre>{JSON.stringify(metrics, null, 2)}</pre>
    </div>
  );
}
