from flask import Flask, render_template, redirect, url_for, flash, request
import json

app = Flask(__name__)


class Bible:
    data = None
    
    def __init__(self, file_path):
        if self.data is None:
            # Load the Bible data from the given file path
            with open(file_path, 'r') as file:
                self.data = json.load(file)
        self.bookmarks = {}
        self.notes = {}
        self.current_book = None
        self.current_chapter = None
        
    def fetch_info(self):
        # Metadata information
        metadata = self.data['metadata']
        return metadata
    
    def fetch_books(self):
        books = {verse['book']: verse['book_name'] for verse in self.data['verses']}
        return sorted(books.items())
    
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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', active_page='home')

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