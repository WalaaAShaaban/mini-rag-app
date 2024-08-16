from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from controllers import DataController, ProjectController

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
    if is_valid:
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)

    project_dir = ProjectController().get_file_path(file_name=file_name)


