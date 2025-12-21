# BookAI Reader

BookAI Reader is a desktop application written in Python that lets you build a personal library of ebooks (PDF, EPUB, MOBI, TXT, DOCX), read them, and use AI to generate summaries and embeddings for smarter reading workflows. The app ships with a simple Tkinter-based UI, a pluggable parsing layer for different formats, and an AI module built on top of modern NLP libraries.[web:6][web:14][web:17][web:24][web:25][web:31][web:34][web:35][web:40]

---

## Features

- Add local books (PDF, EPUB, MOBI, TXT, DOCX) into a persistent library managed as JSON on disk.[web:6][web:14][web:31][web:34]
- Extract text from each format using dedicated parsers (PyMuPDF, EbookLib, mobi, python-docx, etc.).[web:24][web:25][web:31][web:34]
- Read full text in a scrollable viewer within the app.
- Generate AI summaries of the currently open book using a transformer-based summarization model.[web:35][web:40]
- Basic embeddings module scaffold (ready for semantic search / Q&A features later).[web:35][web:40]
- Simple Tkinter UI with:
  - Library list on the left
  - Reader and AI summary panel on the right[web:15]

---

## Project Structure

bookai-reader/
├─ .gitignore
├─ Makefile
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ setup.sh
├─ src/
│ ├─ init.py
│ ├─ main.py # entrypoint
│ ├─ config.py # paths, app config
│ ├─ models.py # Book dataclass
│ ├─ library_manager.py # library persistence
│ ├─ file_parsers/
│ │ ├─ init.py
│ │ ├─ base.py
│ │ ├─ pdf_parser.py
│ │ ├─ epub_parser.py
│ │ ├─ mobi_parser.py
│ │ ├─ txt_parser.py
│ │ └─ docx_parser.py
│ ├─ ai/
│ │ ├─ init.py
│ │ ├─ summarizer.py
│ │ └─ embeddings.py
│ └─ ui/
│ ├─ init.py
│ ├─ main_window.py
│ └─ widgets.py
└─ tests/
├─ init.py
├─ test_parsers.py
├─ test_library_manager.py
└─ test_ai.py


---

## Requirements

All Python dependencies are listed in `requirements.txt`. They include:

- GUI: `tk` (Tkinter bindings).[web:15]
- PDF parsing: `PyMuPDF`, `PyPDF2`.[web:24][web:25]
- EPUB parsing: `EbookLib`, `beautifulsoup4`.[web:14][web:31][web:34]
- MOBI parsing: `mobi`.[web:5]
- DOCX parsing: `python-docx`.
- AI / NLP: `transformers`, `torch`, `sentence-transformers`.[web:29][web:35][web:40]
- Dev tools: `pytest`, `ruff`, `black`.

Ensure you have Python 3.10+ installed.

---

## Setup

### 1. Clone the repository

```
git clone https://github.com/<your-username>/bookai-reader.git
cd bookai-reader
```


### 2. Create virtual environment and install dependencies

You can use the provided `setup.sh`:

```
./setup.sh
```

then, in each new shell:
```
source .venv/bin/activate
```
or manually:
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---