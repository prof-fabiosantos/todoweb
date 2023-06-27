from flask import Flask, jsonify, request, g
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
DATABASE = 'todo.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)")
        db.commit()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, title FROM tasks")
    tasks = [{'id': row[0], 'title': row[1]} for row in cursor.fetchall()]
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    db = get_db()
    cursor = db.cursor()
    task = request.json.get('task')
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (task,))
    db.commit()
    return jsonify({'success': True})

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    db = get_db()
    cursor = db.cursor()
    task = request.json.get('task')
    cursor.execute("UPDATE tasks SET title=? WHERE id=?", (task, task_id))
    db.commit()
    return jsonify({'success': True})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    db.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run()
