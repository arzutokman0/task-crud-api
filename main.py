from typing import Optional
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

# Yeni görev oluşturma modeli
class TaskCreate(BaseModel):
    title: str

# Görev güncelleme modeli (title ve done alanları isteğe bağlı gönderilebilir)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# In-memory sahte veri tabanımız
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

@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    if not task_data.title or task_data.title.strip() == "":
        raise HTTPException(status_code=400, detail="Task title cannot be empty")
    
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": task_data.title.strip(),
        "done": False
    }
    tasks.append(new_task)
    return new_task

# 4. Görev güncelleme endpoint'i (PUT)
@app.put("/tasks/{id}")
def update_task(id: int, task_data: TaskUpdate):
    # Önce görevi bulalım
    target_task = None
    for task in tasks:
        if task["id"] == id:
            target_task = task
            break
            
    # Görev yoksa 404 dön
    if not target_task:
        raise HTTPException(status_code=404, detail=f"Task {id} not found")
        
    # Gövde tamamen boş gönderildiyse 400 dön
    if task_data.title is None and task_data.done is None:
        raise HTTPException(status_code=400, detail="Request body cannot be empty")
        
    # Eğer title gönderildiyse, boş string olup olmadığını kontrol et ve güncelle
    if task_data.title is not None:
        if task_data.title.strip() == "":
            raise HTTPException(status_code=400, detail="Task title cannot be empty")
        target_task["title"] = task_data.title.strip()
        
    # Eğer done gönderildiyse güncelle
    if task_data.done is not None:
        target_task["done"] = task_data.done
        
    return target_task

# 5. Görev silme endpoint'i (DELETE)
@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    for index, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(index)
            return Response(status_code=204)
            
    # Silinecek görev yoksa 404 dön
    raise HTTPException(status_code=404, detail=f"Task {id} not found")