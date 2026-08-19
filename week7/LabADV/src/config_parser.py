import json
from pathlib import Path


class ConfigParser:
    REQUIRED_KEYS = (
        "start_url",
        "max_pages",
        "delay_between_pages",
        "item_container_selector",
        "item_data_selectors",
    )

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)

    def load_config(self) -> dict:
        if not self.config_path.is_file():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with self.config_path.open("r", encoding="utf-8") as config_file:
            config = json.load(config_file)

        self._validate_config(config)
        return config

    def _validate_config(self, config: dict):
        if not isinstance(config, dict):
            raise ValueError("Configuration must be a JSON object")

        for key in self.REQUIRED_KEYS:
            if key not in config:
                raise KeyError(f"Missing required configuration key: '{key}'")

        if not isinstance(config["max_pages"], int) or config["max_pages"] < 1:
            raise ValueError("'max_pages' must be a positive integer")
        if config["delay_between_pages"] < 0:
            raise ValueError("'delay_between_pages' cannot be negative")
        if not isinstance(config["item_data_selectors"], dict):
            raise ValueError("'item_data_selectors' must be an object")
