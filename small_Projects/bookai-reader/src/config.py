from pathlib import Path

APP_NAME = "BookAI Reader"
DATA_DIR = Path.home() / ".bookai_reader"
LIBRARY_DB = DATA_DIR / "library.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)
