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

