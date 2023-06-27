import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    const response = await fetch('http://127.0.0.1:5000/api/tasks');
    const data = await response.json();
    setTasks(data);
  };

  const addTask = async () => {
    if (newTask.trim() !== '') {
      const response = await fetch('http://127.0.0.1:5000/api/tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ task: newTask }),
      });
      if (response.ok) {
        setNewTask('');
        fetchTasks();
      }
    }
  };

  const deleteTask = async (taskId) => {
    const response = await fetch(`http://127.0.0.1:5000/api/tasks/${taskId}`, { method: 'DELETE' });
    if (response.ok) {
      fetchTasks();
    }
  };

  const updateTask = async (taskId, newTitle) => {
    const response = await fetch(`http://127.0.0.1:5000/api/tasks/${taskId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ task: newTitle }),
    });
    if (response.ok) {
      fetchTasks();
    }
  };

  return (
    <div className="App">
      <h1>Lista de Tarefas</h1>
      <div className="task-container">
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Adicionar uma tarefa"
        />
        <button onClick={addTask}>Adicionar</button>
      </div>
      <ul className="task-list">
        {tasks.map((task) => (
          <li key={task.id} className="task-item">
            <input
              type="text"
              value={task.title}
              onChange={(e) => updateTask(task.id, e.target.value)}
              className="task-title"
            />
            <button className="delete-button" onClick={() => deleteTask(task.id)}>
              Excluir
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
