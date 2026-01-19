import os
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI

from src.utils.import_utils import ImportUtils

app = FastAPI(docs_url="/api/docs",
              redoc_url="/api/redoc", openapi_url="/api/openapi.json")


def load_modules_from_directory(directory: str, callback: callable):
    path = os.path.join(os.path.dirname(__file__), directory)
    for file in os.listdir(path):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]
            file_path = os.path.join(path, file)
            module = ImportUtils.import_module_from_path(
                module_name, file_path)
            callback(module)


load_modules_from_directory(
    "controllers", lambda module: app.include_router(module.router, prefix="/api"))

app.mount("/", StaticFiles(directory="src/http/public",
                           html=True), name="public")

uvicorn.run(app, port=int(os.getenv("WEB_PORT", 8000)),
            host=os.getenv("WEB_HOST", "127.0.0.1"))
