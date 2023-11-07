import React, { useState } from "react";
import { GetTasks, PostTasks } from "./api/Axios.js";
import Header from "./componentes/Header.js";
import "./input.css";

function App() {
  
  const [setTasks] = useState([]);

  return (
    <div className="App">
      <title>Lista de Tarefas</title>
      <Header />
      <GetTasks setTasks={setTasks} />
      <PostTasks setTasks={setTasks} />
    </div>
  );

}

export default App;
