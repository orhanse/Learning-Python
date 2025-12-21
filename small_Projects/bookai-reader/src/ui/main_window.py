import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from ..config import APP_NAME
from ..library_manager import LibraryManager
from ..file_parsers import get_parser
from .widgets import BookList


def run_app() -> None:
    root = tk.Tk()
    root.title(APP_NAME)
    root.geometry("900x600")

    app = MainWindow(root)
    root.mainloop()

class MainWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.library = LibraryManager()

        self._build_ui()
        self._load_library()

    
    def _build_ui(self) -> None:
        # Left: library
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        toolbar = tk.Frame(left_frame)
        toolbar.pack(fill=tk.X)

        add_btn = tk.Button(toolbar, text="Add Book", command=self._add_book)
        add_btn.pack(side=tk.LEFT, padx=4, pady=4)

        remove_btn = tk.Button(toolbar, text="Remove", command=self._remove_book)
        remove_btn.pack(side=tk.LEFT, padx=4, pady=4)

        self.book_list = BookList(left_frame, height=25)
        self.book_list.pack(fill=tk.BOTH, expand=True)
        self.book_list.bind("<<TreeviewSelect>>", self._on_select_book)

        # Right: text
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        top_right = tk.Frame(right_frame)
        top_right.pack(fill=tk.BOTH, expand=True)

        self.text_box = tk.Text(top_right, wrap=tk.WORD)
        self.text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(top_right, command=self.text_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_box.config(yscrollcommand=scrollbar.set)

        bottom_right = tk.Frame(right_frame)
        bottom_right.pack(fill=tk.BOTH, expand=False)

        #Add ai summarize here

        self.summary_box = tk.Text(bottom_right, height=8, wrap=tk.WORD)
        self.summary_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _load_library(self) -> None:
        self.book_list.load_books(self.library.list_books())

    def _add_book(self) -> None:
        filetypes = [
            ("Books", "*.pdf *.epub *.mobi *.txt *.docx"),
            ("PDF", "*.pdf"),
            ("EPUB", "*.epub"),
            ("MOBI", "*.mobi"),
            ("Text", "*.txt"),
            ("Word", "*.docx"),
        ]
        filename = filedialog.askopenfilename(title="Select book", filetypes=filetypes)
        if not filename:
            return

        path = Path(filename)
        ext = path.suffix.lower().lstrip(".")
        book = self.library.add_book(path=path, fmt=ext)  # type: ignore
        self.book_list.load_books(self.library.list_books())
        self._open_book(book.id)

    
    def _remove_book(self) -> None:
        sel = self.book_list.selection()
        if not sel:
            return
        book_id = sel[0]
        self.library.remove_book(book_id)
        self.book_list.load_books(self.library.list_books())
        self.text_box.delete("1.0", tk.END)
        self.summary_box.delete("1.0", tk.END)

    
    def _on_select_book(self, event=None) -> None:
        sel = self.book_list.selection()
        if not sel:
            return
        book_id = sel[0]
        self._open_book(book_id)

    def _open_book(self, book_id: str) -> None:
        book = self.library.get_book(book_id)
        if not book:
            return
        parser = get_parser(book.fmt)
        if not parser:
            messagebox.showerror("Error", f"No parser for format: {book.fmt}")
            return

        try:
            text = parser.extract_text(book.path)
        except Exception as exc:  # noqa: BLE001
            messagebox.showerror("Error", f"Failed to open book: {exc}")
            return

        self.text_box.delete("1.0", tk.END)
        self.text_box.insert("1.0", text)
        self.summary_box.delete("1.0", tk.END)