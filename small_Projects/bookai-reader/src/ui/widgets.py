import tkinter as tk
from tkinter import ttk


class BookList(ttk.Treeview):
    def __init__(self, master, **kwargs):
        columns = ("title", "author", "fmt")
        super().__init__(master, columns=columns, show="headings", **kwargs)
        self.heading("title", text="Title")
        self.heading("author", text="Author")
        self.heading("fmt", text="Format")
        self.column("title", width=220)
        self.column("author", width=160)
        self.column("fmt", width=60)

    def load_books(self, books):
        self.delete(*self.get_children())
        for book in books:
            self.insert(
                "",
                "end",
                iid=book.id,
                values=(book.title, book.author or "", book.fmt),
            )
