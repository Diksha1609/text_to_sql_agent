from fastapi import FastAPI

app = FastAPI(title="Text-to-SQL AI Agent")

@app.get("/")
def health():
    return {"status": "ok"}
