from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Literal

BookFormat = Literal["pdf", "epub", "mobi", "txt", "docx"]

@dataclass
class Book:
    id: str
    title: str
    author: Optional[str]
    path: Path
    fmt: BookFormat
