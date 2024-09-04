from flask import Flask, render_template, redirect, url_for, flash, request
import json

app = Flask(__name__)


class Bible:
    data = None
    books_data = None

    @classmethod
    def load_bible_data(cls, bible_file_path, book_file_path):
        if cls.data is None:
            # Load the Bible data from the given file path
            with open(bible_file_path, 'r') as file:
                cls.data = json.load(file)
        if cls.books_data is None:
            # Load the books data from the given file path
            with open(book_file_path, 'r') as books_file:
                cls.books_data = json.load(books_file)
    
    def __init__(self):
        self.bookmarks = {}
        self.notes = {}
        self.current_book = None
        self.current_chapter = None
        
    def fetch_info(self):
        # Metadata information
        metadata = self.data['metadata']
        return metadata
    
    def get_books(self):
        return list(self.books_data.keys())
    
    def get_book_chapters(self, book_name):
        return list(self.books_data.get(book_name, {}).keys())
    
    def get_chapter_verses(self, book_name, chapter):
        chapters = self.books_data.get(book_name, {})
        return chapters.get(chapter, [])
    
    def select_book(self, book_name):
        books = {verse['book_name']: verse['book'] for verse in self.data['verses']}
        if book_name in books:
            self.current_book = books[book_name]
            return book_name
        else:
            return "Book not found."
        
    def select_chapter(self, chapter_number):
        if self.current_book is not None:
            self.current_chapter = chapter_number
            return chapter_number
        else:
            return "Select a book first."
        
    def fetch_chapter(self):
        if self.current_book is not None and self.current_chapter is not None:
            verses = [verse for verse in self.data['verses'] if verse['book'] == self.current_book and verse['chapter'] == self.current_chapter]
            return verses
        else:
            return "Select a book and chapter first."
        
    def add_bookmark(self, book_name, chapter, verse):
        if book_name not in self.bookmarks:
            self.bookmarks[book_name] = []
        self.bookmarks[book_name].append((chapter, verse))
        return f"Bookmark added: {book_name} {chapter}:{verse}"
    
    def fetch_bookmarks(self):
        return self.bookmarks
    
    def add_note(self, book_name, chapter, verse, text):
        if book_name not in self.notes:
            self.notes[book_name] =[]
        self.notes[book_name].append({'chapter': chapter, 'verse': verse, 'text': text})
        return f"Note added: {book_name} {chapter}:{verse} - {text}"
    
    def fetch_notes(self):
        return self.notes

# Load the data once
Bible.load_bible_data('bible.json', 'books.json') 


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    bible = Bible()
    metadata = bible.fetch_info()
    books = bible.get_books()
    chapters = {book: bible.get_book_chapters(book) for book in books}
    verses = {}
    for book, chapters_list in chapters.items():
        for chapter in chapters_list:
            verses[chapter] = list(bible.get_chapter_verses(book, chapter))
    
    selected_book = None
    selected_chapter = None
    selected_verse = None
    selected_verse_text = None
    chapter_data = None
    
    if request.method == 'POST':
        selected_book = request.form.get('book_name', '').strip()
        selected_chapter_str = request.form.get('chapter', '').strip()
        selected_verse_str = request.form.get('verse', '').strip()

        # Handle selected chapter and verse safely
        try:
            if selected_chapter_str:
                selected_chapter = int(selected_chapter_str)
        except ValueError:
            selected_chapter = None

        try:
            if selected_verse_str:
                selected_verse = int(selected_verse_str)
        except ValueError:
            selected_verse = None
        
        bible.select_book(selected_book)
        if selected_chapter is not None:
            bible.select_chapter(selected_chapter)
        
        if selected_verse is not None:
            verses_data = bible.fetch_chapter()
            if verses_data:
                selected_verse_text = next((verse['text'] for verse in verses_data if verse['verse'] == selected_verse), "Verse not found.")
        elif selected_chapter is not None:
            chapter_data = bible.fetch_chapter()
    
    return render_template('home.html',
                           active_page='home',
                           bible=bible,
                           metadata=metadata,
                           books=books,
                           chapters=chapters,
                           verses=verses,
                           selected_book=selected_book,
                           selected_chapter=selected_chapter,
                           selected_verse=selected_verse,
                           selected_verse_text=selected_verse_text,
                           chapter_data=chapter_data)


@app.route('/search')
def search():
    return render_template('search.html', active_page='search')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

# @app.route('/feedback')
# def feedback():
#     return render_template('feedback.html', active_page='feedback')

# Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)