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

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from polaris.api import tasks
from polaris.models import base
from polaris.database import engine

# Initialize database tables at startup
# Creates all SQLAlchemy model tables if they don't exist
base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Polaris", description="ADHD-friendly project management", version="0.1.0"
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
