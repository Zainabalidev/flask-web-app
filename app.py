import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# In-memory database (resets on restart)
tasks = [
    {"id": 1, "title": "Automate Deployment", "done": False},
    {"id": 2, "title": "Master Flask", "done": True}
]

# Helper function to generate unique IDs
def get_next_id():
    return max([t["id"] for t in tasks], default=0) + 1


#  GET all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "success": True,
        "tasks": tasks
    }), 200


#  POST add new task
@app.route("/tasks", methods=["POST"])
def add_task():
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Missing 'title' in request body"}), 400

    if not isinstance(request.json['title'], str):
        return jsonify({"error": "title must be a string"}), 400

    new_task = {
        "id": get_next_id(),
        "title": request.json['title'],
        "done": False
    }

    tasks.append(new_task)

    return jsonify({
        "success": True,
        "task": new_task
    }), 201


#  DELETE task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    tasks = [t for t in tasks if t["id"] != task_id]

    return jsonify({
        "success": True,
        "message": f"Task {task_id} deleted"
    }), 200


#  Health check (for CI/CD / Docker / load balancers)
@app.route("/health")
def health_check():
    return jsonify({"status": "healthy"}), 200


#  About / environment info
@app.route("/about")
def about():
    return jsonify({
        "status": "Running",
        "env": os.getenv('FLASK_ENV', 'not set'),
        "debug_mode": os.getenv('DEBUG', 'not set')
    })


#  Run server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)