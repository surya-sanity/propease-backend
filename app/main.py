from fastapi import FastAPI, APIRouter

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")

router = APIRouter(prefix="/api", tags=["API"])


@router.get("/health")
def health():
    """Endpoint to check the health status of the application."""
    return {"status": "ok"}


app.include_router(router)
