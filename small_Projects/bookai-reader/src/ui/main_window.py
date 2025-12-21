import tkinter as tk
from pathlib import Path

from ..config import APP_NAME


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