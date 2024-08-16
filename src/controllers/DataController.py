from .BaseController import BaseController
from fastapi import UploadFile
from models.enums import ResponseSignal

class DataController(BaseController):
    
    def __init__(self) -> None:
        super().__init__()
        self.scale_size = 10485760 #convert mb to byte

    def validate_upload_file(self, file:UploadFile)-> bool:
        if file.content_type not in self.get_settings.FILE_UPLOAD_EXTENSTION:
            return False, ResponseSignal.FILE_INVALID_EXTENSION.value
        if file.size > self.get_settings.FILE_MAX_SIZE * self.scale_size:
            return False, ResponseSignal.FILE_INVALID_SIZE.value
        return True, ResponseSignal.FILE_VALID.value
