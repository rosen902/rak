from pathlib import Path
import subprocess
import toml

class RustEnvManager:
    DEPS = {
        "axum": "\"0.7\"",
        "tokio": "{{ version= \"1\", features = [\"full\"] }}",
        "tower": "\"0.4\""
    }

    def __init__(self, path: Path):
        self.path = path
        self.cargo_toml_path = self.path / "Cargo.toml"

        self.init_env_if_not_exists()
        self.__load_cargo_file()
        self.add_base_deps()

    def __load_cargo_file(self):
        with open(self.cargo_toml_path, 'r') as file:
            self.cargo_data = toml.load(file)

    def init_env_if_not_exists(self):
        if(not self.cargo_toml_path.exists()):
            subprocess.run(["cargo", "init"], cwd=self.path)

    def add_base_deps(self):
        for key, value in DEPS:
            
            
    
    def __overwrite_cargo_file(self):



