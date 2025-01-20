from fastapi import FastAPI
from services.service import router as milvus_router

app = FastAPI(
    title="Milvus API Service",
    description="API for managing Milvus collections with create, insert, delete, and edit functionality.",
    version="1.0.0"
)

# Include the router
app.include_router(milvus_router, prefix="/milvus", tags=["Milvus Operations"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
