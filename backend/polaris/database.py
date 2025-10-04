"""Database configuration and session management for Polaris.

This module sets up the SQLAlchemy engine, session factory, and declarative base
for database operations. It provides dependency injection support for FastAPI
endpoints through the get_db() generator function.

Key components:
    - engine: SQLAlchemy database engine instance
    - SessionLocal: Session factory for creating database sessions
    - Base: Declarative base class for ORM models
    - get_db(): FastAPI dependency for database session injection

Usage:
    Import Base for model definitions:
        from polaris.database import Base

        class User(Base):
            __tablename__ = "users"
            ...

    Use get_db() as a FastAPI dependency:
        @app.get("/users")
        def get_users(db: Session = Depends(get_db)):
            return db.query(User).all()
"""

from collections.abc import Iterator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from polaris.config import settings

# Database engine configured from settings
engine = create_engine(settings.DATABASE_URL)

# Session factory with autocommit disabled for explicit transaction control
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base for ORM model definitions
Base = DeclarativeBase()


def get_db() -> Iterator[Session]:
    """Provide a database session for FastAPI dependency injection.

    Creates a new SQLAlchemy session for each request and ensures proper
    cleanup after the request completes. This function is designed to be
    used with FastAPI's Depends() for automatic session management.

    Yields:
        Session: SQLAlchemy database session

    Example:
        @app.get("/items")
        def read_items(db: Session = Depends(get_db)):
            return db.query(Item).all()

    Note:
        The session is automatically closed in the finally block, ensuring
        connections are properly released even if an error occurs.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
