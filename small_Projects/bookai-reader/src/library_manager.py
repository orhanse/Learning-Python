import json
import uuid
from pathlib import Path
from typing import Dict, List

from .config import LIBRARY_DB
from .models import Book, BookFormat

class LibraryManager:
    def __init__(self, db_path: Path | None = None) -> None:
        self.db_path = db_path or LIBRARY_DB
        self._books: Dict[str, Book] = {}
        self.load()

    def load(self) -> None:
        if not self.db_path.exists():
            self._books = {}
            return
        data = json.loads(self.db_path.read_text(encoding="utf-8"))
        self._books = {
            b["id"]: Book(
                id=b["id"],
                title=b["title"],
                author=b.get("author"),
                path=Path(b["path"]),
                fmt=b["fmt"],
            )
            for b in data
        }

    def save(self) -> None:
        data = [
            {
                "id": b.id,
                "title": b.title,
                "author": b.author,
                "path": str(b.path),
                "fmt": b.fmt,
            }
            for b in self._books.values()
        ]
        self.db_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def list_books(self) -> List[Book]:
        return list(self._books.values())

    def add_book(self, path: Path, title: str | None = None,
                 author: str | None = None, fmt: BookFormat | None = None) -> Book:
        if fmt is None:
            fmt = path.suffix.lower().lstrip(".")  # type: ignore
        book_id = str(uuid.uuid4())
        book = Book(
            id=book_id,
            title=title or path.stem,
            author=author,
            path=path,
            fmt=fmt,  # type: ignore
        )
        self._books[book_id] = book
        self.save()
        return book

    def get_book(self, book_id: str) -> Book | None:
        return self._books.get(book_id)

    def remove_book(self, book_id: str) -> None:
        if book_id in self._books:
            del self._books[book_id]
            self.save()
