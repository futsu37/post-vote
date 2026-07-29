import { useState, useEffect } from "react";
import "./App.css";

type ApiResponse = {
  message: string;
};  

function App() {
  const [data, setData] = useState<ApiResponse | null>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch("http://localhost:8000/");
        const result = await response.json();

        setData(result);
      } catch (err) {
        console.error(err);
      }
    }

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>Hello, World!</h1>
      <p>{data?.message}</p>
    </div>
  );
}

export default App;