"""Polaris API - ADHD-friendly project management system.

This module serves as the main entry point for the Polaris FastAPI application.
It configures the application instance, middleware, database initialization,
and route handlers for an ADHD-friendly task management system.

Key components:
    - FastAPI application instance with metadata
    - CORS middleware for cross-origin requests
    - Database table creation on startup
    - Task management API routes
    - Health check endpoints

Usage:
    Run the application using uvicorn:
        $ uvicorn polaris.main:app --reload
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from polaris.api import tasks
from polaris.models import base
from polaris.database import get_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup and shutdown events.

    Attempts to initialize database tables on startup. If database
    connection fails, logs a warning but allows app to start for
    health checks and non-database endpoints.
    """
    # Startup: Try to initialize database tables
    try:
        base.Base.metadata.create_all(bind=get_engine())
    except Exception as e:
        # Log warning but don't crash - allows health checks to work
        print(f"Warning: Could not initialize database: {e}")
        print("App will start but database-dependent endpoints may fail.")
    yield
    # Shutdown: cleanup would go here if needed


app = FastAPI(
    title="Polaris",
    description="ADHD-friendly project management",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS middleware to allow Flutter app to communicate with the API
# Note: This is a permissive configuration suitable for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:*",
        "http://127.0.0.1:*",
    ],  # TODO: Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route handlers
app.include_router(tasks.router, prefix="/api/tasks", tags=["tasks"])


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint providing basic API information.

    Returns:
        dict: API name and version information.
    """
    return {"message": "Polaris API", "version": "0.1.0"}


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint for monitoring and orchestration.

    Used by deployment platforms and load balancers to verify
    the application is running and responsive.

    Returns:
        dict: Status indicator showing the service is healthy.
    """
    return {"status": "healthy"}
