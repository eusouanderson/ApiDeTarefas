import React, { useEffect, useState } from "react";
import axios from "axios";

const URL_API = "http://localhost:8000";
const bearerToken = "eusouanderson:CQ5mE4c0ZtR07sBB"; 

export function GetTasks() {
  const [tarefas, setTasks] = useState([]);

  useEffect(() => {
    axios
      .get(URL_API + "/api/", {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      })
      .then((response) => {
        setTasks(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);
  
}
export function DeleteTasks() {
  const [tarefas, setTasks] = useState([]);

}
export function PostTasks() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [tarefas, setTasks] = useState([]); 

  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };

  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };

  const handleSubmit = () => {
   
    const newTask = {
      title: title,
      description: description,
    };

    axios
      .post(URL_API + "/api/", newTask, {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      })
      .then((response) => {
        console.log("Tarefa criada com sucesso!", response.data);
        setTasks([...tarefas, response.data]);
      })
      .catch((error) => {
        console.error("Erro ao criar a tarefa", error);
      });
  };

  useEffect(() => {
    
    axios
      .get(URL_API + "/api/", {
        headers: {
          Authorization: `Bearer ${bearerToken}`,
        },
      })
      .then((response) => {
        setTasks(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div className="bg-gray-900 text-white p-8 rounded-lg shadow-lg">
      <h1 className="text-3xl font-bold mb-4">Insira sua Tarefa</h1>
      <div className="flex space-x-4 mb-4">
        <input
          type="text"
          placeholder="Título da Tarefa"
          value={title}
          onChange={handleTitleChange}
          className="w-1/2 bg-gray-800 text-white py-2 px-3 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
        />
        <input
          type="text"
          placeholder="Descrição da Tarefa"
          value={description}
          onChange={handleDescriptionChange}
          className="w-1/2 bg-gray-800 text-white py-2 px-3 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
        />
        <button
          onClick={handleSubmit}
          className="bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring focus:border-blue-300"
        >
          Enviar
        </button>
      </div>
      <div>
        <ul>
          {tarefas.map((tarefa) => (
            <li key={tarefa.id} className="mb-4 p-4 bg-gray-800 rounded-lg">
              <h3 className="text-xl font-semibold">{tarefa.title}</h3>
              <p className="text-gray-300">{tarefa.description}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>

  );
}


