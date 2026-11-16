# W2 · A1 — Build your first CRUD API

A lightweight, in-memory RESTful Task Management API built with Python and FastAPI. This project implements all four core CRUD operations (Create, Read, Update, Delete), input validation, proper HTTP status codes, and interactive Swagger UI documentation.

## 🛠️ Tech Stack
* Language: Python 3.10+
* Framework: FastAPI
* Server: Uvicorn
* Validation: Pydantic
* Documentation: Swagger UI (/docs)

---

## 📌 API Endpoints

| CRUD Operation | HTTP Method | Endpoint | Description | Status Codes |
| :--- | :--- | :--- | :--- | :--- |
| **Metadata** | `GET` | `/` | Returns API name, version, and endpoints | `200 OK` |
| **Health Check** | `GET` | `/health` | Verifies server status | `200 OK` |
| **Read (All)** | `GET` | `/tasks` | Lists all tasks in memory | `200 OK` |
| **Read (Single)** | `GET` | `/tasks/{id}` | Retrieves a single task by ID | `200 OK`, `404 Not Found` |
| **Create** | `POST` | `/tasks` | Creates a new task | `201 Created`, `400 Bad Request` |
| **Update** | `PUT` | `/tasks/{id}` | Updates task title and/or done status | `200 OK`, `400 Bad Request`, `404 Not Found` |
| **Delete** | `DELETE` | `/tasks/{id}` | Deletes a task by ID | `204 No Content`, `404 Not Found` |

---

## 💻 Example curl Output

Creating a new task via POST /tasks:

{"id":4,"title":"Buy milk","done":false}
