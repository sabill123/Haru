from fastapi import FastAPI
from .api.routes import api_router
from .database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Haru API")
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)