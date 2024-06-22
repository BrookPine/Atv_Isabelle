from fastapi import FastAPI
from app.controllers import task_controllers

app = FastAPI()

app.include_router(task_controllers.router)
