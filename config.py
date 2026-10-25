import configparser
from pathlib import Path


CONFIG_PATH = (
    Path(__file__).resolve().parent.parent
    / "config"
    / "config.ini"
)


def load_config():
    """Load application configuration from config.ini."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_PATH}"
        )

    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    if "database" not in config:
        raise ValueError("Missing [database] section in config.ini")

    return config