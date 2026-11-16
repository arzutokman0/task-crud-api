from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic modeli: Dışarıdan (POST ile) gelecek verinin kalıbını belirliyoruz
class TaskCreate(BaseModel):
    title: str

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

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

# 3. Yeni görev oluşturma endpoint'i (POST)
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    # İş Kuralı: Başlık boş mu veya sadece boşluktan mı ibaret kontrol et
    if not task_data.title or task_data.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    
    # Yeni ID'yi hesapla (Eğer liste boşsa 1, doluluğa göre son ID + 1)
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    
    # Yeni görev sözlüğünü oluştur
    new_task = {
        "id": new_id,
        "title": task_data.title.strip(),
        "done": False
    }
    
    # Listemize ekle
    tasks.append(new_task)
    
    # Oluşturulan yeni görevi ve 201 kodunu dön
    return new_task