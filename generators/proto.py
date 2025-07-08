import xml.etree.ElementTree as ET
from pathlib import Path
from logger import Logger

class ProtoGenerator:
    def __init__(self, models_folder_path : Path):
        self.models_folder = models_folder_path
        self.models = {}
        self.logger = Logger()

    def __load_model_file(self, entry : Path):
        tree = ET.parse(str(entry))
        root = tree.getroot()
        for child in root:
            print(child.tag)
    
    def load_models(self):
        for entry in self.models_folder.iterdir():
            if entry.is_file():
                self.__load_model_file(entry)