# Bible App

## Overview

The Bible App consists of two versions: a terminal-based application and a web-based application. Both versions allow you to interact with Bible text, search for keywords, add bookmarks, and make notes. The terminal-based app operates in a command-line environment, while the web-based app provides a graphical interface accessible via a web browser.

### Terminal-Based Bible App

The terminal-based Bible app allows you to navigate through the Bible, search for keywords, add bookmarks, and make notes on specific verses. It uses a JSON file containing the Bible text and metadata.

#### Features

- Display Bible metadata
- List all books in the Bible
- Select a specific book and chapter
- Display the verses in the selected chapter
- Search for keywords in the Bible
- Add bookmarks to specific verses
- List all bookmarks
- Add notes to specific verses
- List all notes

#### Getting Started

##### Prerequisites

- Python 3.x

##### Installation

1. Clone this repository or download the script and the `reformatted_bible.json` file.
2. Enter the project directory
   ```sh
   cd bibleapp
   ```

3. Ensure you have the JSON file named `reformatted_bible.json` in the same directory as the script.

##### Usage

1. Run the script:

   ```sh
   python bibleapp.py
   ```

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

### Web-Based Bible App

The web-based Bible app provides a user-friendly interface for interacting with Bible text through a web browser. It includes features such as theme toggling, search functionality, and a responsive layout.

#### Features

- [x] Display Bible verses and metadata in a web interface
- [ ] Search for keywords in the Bible
- [ ] Add and view bookmarks and notes via the web interface
- [x] Toggle between light and dark modes
- [x] Responsive design for various screen sizes

#### Getting Started

##### Prerequisites

- Python 3.x
- Flask (for running the web server)

##### Installation

1. Clone this repository or download the project files.
   To clone this repository, run the following command in your terminal:

   ```sh
   git clone https://github.com/Cartha007/bibleapp.git
   ```

2. Enter the project directory
   ```sh
   cd bibleapp/webversion
   ```

3. Ensure you have the JSON file named `bible.json` and `books.json` in the project directory.
4. Install the required Python packages using pip:

   ```sh
   pip install -r requirements.txt
   ```

##### Running the Web Application

1. Run the flask application:

   ```sh
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the web-based Bible app.

##### Web Version Interface

- [ ] Search: Use the search bar to find specific Bible verses or keywords.
- [ ] Bookmarks & Notes: Add and view bookmarks and notes directly from the web interface.
- [x] Theme Toggle: Switch between light and dark modes using the toggle button.

##### Notes

- Ensure that the reformatted_bible.json file is located in the project directory for the terminal-based app.
- For a seamless experience, regularly update the `requirements.txt` file with any additional dependencies.