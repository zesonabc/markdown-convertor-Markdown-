from pathlib import Path
import platform

def get_config_path():
    system = platform.system()
    if system == "Windows":
        return Path.home() / "AppData/Local/mdconvert"
    elif system == "Darwin":
        return Path.home() / "Library/Application Support/mdconvert"
    else:
        return Path.home() / ".config/mdconvert"