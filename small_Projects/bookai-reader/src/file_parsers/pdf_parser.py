from pathlib import Path
import fitz  # PyMuPDF

from .base import BaseParser

class PdfParser(BaseParser):
    def extract_text(self, path: Path) -> str:
        text_parts: list[str] = []
        with fitz.open(path) as doc:
            for page in doc:
                text_parts.append(page.get_text())
        return "\n".join(text_parts)
