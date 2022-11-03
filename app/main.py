from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware

from .handlers.http_error import http_error_handler
from .services.base import create_database
from .routers import auth, salaries, users
from .database import seeding

app = FastAPI()

create_database()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(salaries.router)

# Add exception handlers
app.add_exception_handler(HTTPException, http_error_handler)

# Allow cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Applications!"}
