import React, { useState } from "react";
import { GetTasks, PostTasks } from "./api/Axios.js";
import "./input.css";

function App() {
  
  const [tasks, setTasks] = useState([]);

  return (
    <div className="App">
      <title>Lista de Tarefas</title>
      <GetTasks setTasks={setTasks} />
      <PostTasks setTasks={setTasks} />
    </div>
  );

}

export default App;
