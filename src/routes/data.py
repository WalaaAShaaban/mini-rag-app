from fastapi import FastAPI, APIRouter, Depends, UploadFile
from helpers.config import Settings, get_settings
from controllers import DataController

data_route = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_route.post("/upload/{file_name}")
async def upload_file(file_name:str, 
                      file:UploadFile, 
                      app_settings:Settings = Depends(get_settings)):
    
    is_valid, result = DataController().validate_upload_file(file=file)
    return result

