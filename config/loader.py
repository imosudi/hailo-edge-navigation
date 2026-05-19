import yaml
from pathlib import Path


class ConfigLoader:

    @staticmethod
    def load(path: str):
        with open(Path(path), "r") as f:
            return yaml.safe_load(f)