from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory (bellekte tutulan) sahte veri tabanımız
tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Learn FastAPI", "done": True},
    {"id": 3, "title": "Commit to GitHub", "done": False}
]

@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

# 1. Tüm görevleri listeleme endpoint'i
@app.get("/tasks")
def get_tasks():
    return tasks

# 2. ID'ye göre tek bir görev getirme endpoint'i ({id} bir Path Parameter'dır)
# 2. ID'ye göre tek bir görev getirme endpoint'i
@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
            
    # DİKKAT: return yerine raise kullandık!
    raise HTTPException(status_code=404, detail=f"Task {id} not found")