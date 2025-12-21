from abc import ABC, abstractmethod
from pathlib import Path

class BaseParser(ABC):
    @abstractmethod
    def extract_text(self, path: Path) -> str:
        ...
