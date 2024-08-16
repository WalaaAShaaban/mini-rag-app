from enum import Enum
class ResponseSignal(Enum):
    FILE_INVALID_EXTENSION = "Invalid file extension"
    FILE_INVALID_SIZE = "File size is too large"
    FILE_VALID = "File is valid"
    
