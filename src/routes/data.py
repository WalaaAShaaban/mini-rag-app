from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from controllers import DataController, ProjectController
import aiofiles
import os

data_route = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_route.post("/upload/{file_name}")
async def upload_file(file_name:str, 
                      file:UploadFile, 
                      app_settings:Settings = Depends(get_settings)):
    
    is_valid, result = DataController().validate_upload_file(file=file)
    if not is_valid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=result)
    
    project_dir, result = ProjectController().get_project_path(project_id=file_name)
    file_path = os.path.join(project_dir, file.filename)

    async with aiofiles.open(file_path, "wb") as f:
        while chunk := await file.read(app_settings.FILE_DEFULT_CHUNK_SIZE):
            await f.write(chunk)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
