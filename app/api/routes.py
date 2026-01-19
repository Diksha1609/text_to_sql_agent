from fastapi import FastAPI

app = FastAPI(
    title="Text-to-SQL AI Agent",
    description="AI Agent that converts natural language to SQL and generates analytics",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Text-to-SQL Agent is live 🚀"
    }
