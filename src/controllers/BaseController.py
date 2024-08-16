from helpers.config import get_settings

class BaseController:
    def __init__(self) -> None:
        self.get_settings = get_settings()