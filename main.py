from fastapi import FastAPI

app = FastAPI()

# Stage 0'dan kalan kök dizin
@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

# Stage 1 ile eklediğimiz sağlık kontrolü endpoint'i
@app.get("/health")
def health_check():
    return {"status": "ok"}