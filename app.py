import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# App configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# In-memory database (resets when server restarts)
tasks = [
    {"id": 1, "title": "Automate Deployment", "completed": False},
    {"id": 2, "title": "Master Flask", "completed": True}
]


# Generate unique task IDs
def get_next_id():
    return max([task["id"] for task in tasks], default=0) + 1


# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Task Management API",
        "version": "1.0",
        "status": "running",
        "endpoints": {
            "GET /tasks": "Retrieve all tasks",
            "POST /tasks": "Create a new task",
            "DELETE /tasks/<id>": "Delete a task",
            "GET /health": "Health check",
            "GET /about": "Application information"
        }
    }), 200


# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "success": True,
        "count": len(tasks),
        "tasks": tasks
    }), 200


# Create a new task
@app.route("/tasks", methods=["POST"])
def add_task():

    # Validate JSON body
    if not request.json:
        return jsonify({
            "success": False,
            "error": "Request body must be JSON"
        }), 400

    # Validate title existence
    if "title" not in request.json:
        return jsonify({
            "success": False,
            "error": "Missing 'title' field"
        }), 400

    title = request.json["title"]

    # Validate title type
    if not isinstance(title, str):
        return jsonify({
            "success": False,
            "error": "Title must be a string"
        }), 400

    # Validate empty title
    if not title.strip():
        return jsonify({
            "success": False,
            "error": "Title cannot be empty"
        }), 400

    # Create task
    new_task = {
        "id": get_next_id(),
        "title": title.strip(),
        "completed": False
    }

    tasks.append(new_task)

    return jsonify({
        "success": True,
        "message": "Task created successfully",
        "task": new_task
    }), 201


# Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks

    task = next((task for task in tasks if task["id"] == task_id), None)

    if not task:
        return jsonify({
            "success": False,
            "error": "Task not found"
        }), 404

    tasks = [task for task in tasks if task["id"] != task_id]

    return jsonify({
        "success": True,
        "message": f"Task {task_id} deleted successfully"
    }), 200


# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy"
    }), 200


# About endpoint
@app.route("/about", methods=["GET"])
def about():
    return jsonify({
        "application": "Flask Task Management API",
        "environment": os.getenv("FLASK_ENV", "production"),
        "debug_mode": os.getenv("DEBUG", "False")
    }), 200


# Run application locally
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )