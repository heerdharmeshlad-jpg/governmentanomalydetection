from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.user import User

from app.routers.auth import router as auth_router
from app.routers.dashboard import router as dashboard_router
from app.routers.projects import router as projects_router
from app.routers.cases import router as cases_router
from app.routers.vendors import router as vendors_router
from app.routers.reports import router as reports_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Government Anomaly Detection API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://governmentanomalydetection.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/api/v1")
app.include_router(dashboard_router, prefix="/api/v1")
app.include_router(projects_router, prefix="/api/v1")
app.include_router(cases_router, prefix="/api/v1")
app.include_router(vendors_router, prefix="/api/v1")
app.include_router(reports_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "message": "Government Anomaly Detection API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
