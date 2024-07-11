# Terminal-Based Bible App

## Overview

This terminal-based Bible app allows you to navigate through the Bible, search for keywords, add bookmarks, and make notes on specific verses. It uses a JSON file containing the Bible text and metadata.

## Features

- Display Bible metadata
- List all books in the Bible
- Select a specific book and chapter
- Display the verses in the selected chapter
- Search for keywords in the Bible
- Add bookmarks to specific verses
- List all bookmarks
- Add notes to specific verses
- List all notes

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository or download the script and the `bible.json` file.
2. Ensure you have the JSON file named `bible.json` in the same directory as the script.

### Usage

1. Run the script:

   ```sh
   python bible_app.py

2. Enter commands to interact with the app. The available commands are:

    - `info`: Display Bible metadata
    - `books`: List all books in the Bible
    - `book [book_name]`: Select a specific book by its name (e.g., `book Genesis`)
    - `chapter [chapter_number]`: Select a specific chapter in the selected book (e.g., `chapter 1`)
    - `display`: Display the verses in the selected chapter
    - `search [keyword]`: Search for a keyword in the Bible (e.g., `search light`)
    - `bookmark [book_name] [chapter] [verse]`: Add a bookmark to a specific verse (e.g., `bookmark Genesis 1 1`)
    - `bookmarks`: List all bookmarks
    - `note [book_name] [chapter] [verse] [text]`: Add a note to a specific verse (e.g., `note Genesis 1 1 This is the beginning`)
    - `notes`: List all notes
    - `quit`: Quit the app

