import xml.etree.ElementTree as ET
from pathlib import Path
from logger import Logger
import re

class RakEnum:
    def __init__(self, enum_name : str) -> None:
        self.name = enum_name
        self.values = []

    def add_value(self, enum_value : str) -> None:
        self.values.append(enum_value.upper())


class RakStruct:
    def __init__(self, typename : str) -> None:
        self.name = typename
        self.fields = []
    
    def add_field(self, name : str, field_type : str, array : bool, optional : bool) -> None:
        self.fields.append(name, field_type, array, optional)


class RakCompileUnit:
    def __init__(self, name) -> None:
        self.name = name
        self.structs = {}
        self.enums = {}

    def add_struct(self, rak_struct : RakStruct) -> None:
        self.structs[rak_struct.name] = rak_struct
    
    def add_enum(self, rak_enum : RakEnum) -> None:
        self.enums[rak_enum.name] = rak_enum


class RakTypesRepo:
    def __init__(self):
        self.compile_units = {}
    
    def add_unit(self, compile_unit : RakCompileUnit):
        self.compile_units[compile_unit.name] = compile_unit
    

class ProtoGenerator:
    
    TYPE_PATTERN = r'^([A-Za-z][A-Za-z0-9]*)(\[\])?(\?)?$'

    def __init__(self, models_folder_path : Path) -> None:
        self.models_folder = models_folder_path
        self.models = {}
        self.logger = Logger()

    def __check_struct_fields(self, elem : ET.Element) -> bool:
        for field in elem:
            field_attributes = field.attrib
            if "type" not in field_attributes:
                return False
            field_name = field.tag
            match = re.fullmatch(self.TYPE_PATTERN, )

    def __is_correct_typedef(self, elem : ET.Element) -> bool:
        attributes = elem.attrib
        if "typedef" not in attributes:
            return False
        typedef_value = attributes["typedef"]
        if typedef_value not in ["struct", "enum"]:
            return False
        if len(attributes) > 1:
            self.logger.warn(f"Some attributes will be ignored on typedef : {elem.tag}")
        if typedef_value == "struct":
            return self.__check_struct_fields(elem)
        
        

    def __load_typedef(self, child : ET.Element):
        pass

    def __load_model_file(self, entry : Path):
        tree = ET.parse(str(entry))
        root = tree.getroot()
        for child in root:
            if(self.__is_correct_typedef(child)):
                pass
    
    def load_models(self):
        for entry in self.models_folder.iterdir():
            if entry.is_file():
                self.__load_model_file(entry)