from .base import BaseParser
from .pdf_parser import PdfParser

PARSERS = {
    "pdf": PdfParser()
}

def get_parser(ext: str) -> BaseParser | None:
    return PARSERS.get(ext.lower())
