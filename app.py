import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    # Fetch host and port from environment variables with defaults
    host = os.getenv("LISTEN", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    
    # Run the FastAPI app with Uvicorn
    uvicorn.run(app, host=host, port=port)
