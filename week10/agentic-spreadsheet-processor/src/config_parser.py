import json


class ConfigParser:
    def __init__(self, config_file_path: str):
        self.config_file_path = config_file_path

    def load_config(self) -> dict:
        with open(self.config_file_path, "r", encoding="utf-8") as config_file:
            return json.load(config_file)