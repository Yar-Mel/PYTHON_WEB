"""
FastAPI Application Configuration

This module configures a FastAPI application with routes, middleware, and event handlers.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import contacts, auth, users
from src.middlewares.middlewares import (
    startup_event,
    limit_access_by_ip_middleware,
    ban_ips_middleware,
    user_agent_ban_middleware,
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5432",
    "http://localhost:6379",
]

app = FastAPI()

app.include_router(auth.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")
app.include_router(users.router, prefix="/api")

app.add_event_handler("startup", startup_event)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.middleware("http")(limit_access_by_ip_middleware)
app.middleware("http")(ban_ips_middleware)
app.middleware("http")(user_agent_ban_middleware)
