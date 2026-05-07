# Flask Task Management API (Dockerized + CI/CD)

##  Overview

This project is a RESTful API for task management built with Flask.
It demonstrates core DevOps practices including containerization, CI/CD automation, and cloud deployment.

---

##  Tech Stack

* **Backend:** Flask (Python)
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Deployment:** Render
* **Server:** Gunicorn
* **Environment Management:** .env

---

##  Features

* CRUD operations for tasks
* Containerized application using Docker
* Automated CI/CD pipeline with GitHub Actions
* Production-ready deployment using Gunicorn
* Environment variable configuration with `.env`

---

## 🐳 Docker Setup

### Build the image

```bash
docker build -t flask-task-app .
```

### Run the container

```bash
docker run -d -p 8080:8080 flask-task-app
```

---

##  CI/CD Pipeline

The project uses GitHub Actions to:

* Automatically build the Docker image
* Run basic checks/tests
* Prepare the app for deployment

Workflow file:

```
.github/workflows/main.yml
```

---

##  Deployment

The application is deployed on **Render**.

Steps:

1. Connect GitHub repository to Render
2. Configure environment variables
3. Deploy using Docker container

---

##  Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your_secret_key
PORT=8080
```

---

##  API Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| GET    | /tasks      | Get all tasks   |
| POST   | /tasks      | Create new task |
| PUT    | /tasks/<id> | Update task     |
| DELETE | /tasks/<id> | Delete task     |

---


##  DevOps Focus

This project highlights:

* Containerized application lifecycle
* CI/CD pipeline automation
* Cloud deployment workflow
* Environment configuration best practices

---

##  Repository

https://github.com/Zainabalidev/flask-web-app.git
