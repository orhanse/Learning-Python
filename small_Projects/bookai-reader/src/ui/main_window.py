import tkinter as tk
from tkinter import filedialog
from pathlib import Path

from ..config import APP_NAME
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

        self._build_ui()

    
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
        print('Booked added: ', path)

    
    def _remove_book(self) -> None:
        print('Booked removed.')

    
    def _on_select_book(self, event=None) -> None:
        sel = self.book_list.selection()
        if not sel:
            return
        book_id = sel[0]
        self._open_book(book_id)