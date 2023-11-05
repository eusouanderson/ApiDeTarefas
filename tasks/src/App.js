import React from "react";
import { PostTasks } from "./api/Axios.js";
import "./input.css";

function App() {
  return (
    <div className="App">
      <title>Lista de Tarefas</title>
      <PostTasks />
    </div>
  );
}

export default App;
