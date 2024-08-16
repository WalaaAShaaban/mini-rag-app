from .BaseController import BaseController

class ProjectController(BaseController):
    def __init__(self):
        super().__init__()

    
    def get_file_path(self, file_name:str):
        self.project_dir = os.path.join(self.file_dir, file_name)

        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)
        return self.project_dir
