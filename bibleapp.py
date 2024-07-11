import json

class BibleApp:
    def __init__(self, file_path):
        # Load the JSON data from the given file path
        with open(file_path, 'r') as file:
            self.data = json.load(file)
        
        # Initialize bookmarks and notes dictionaries
        self.bookmarks = {}
        self.notes = {}
        self.current_book = None
        self.current_chapter = None
    
    def display_info(self):
        # Display metadata information
        metadata = self.data['metadata']
        for key, value in metadata.items():
            print(f"{key}: {value}")
    
    def list_books(self):
        # List all books available in the Bible
        books = {verse['book']: verse['book_name'] for verse in self.data['verses']}
        for book_id, book_name in sorted(books.items()):
            print(f"{book_id}: {book_name}")
    
    def select_book(self, book_name):
        # Select a book by its name
        books = {verse['book_name']: verse['book'] for verse in self.data['verses']}
        if book_name in books:
            self.current_book = books[book_name]
            print(f"Selected book: {book_name}")
        else:
            print("Book not found.")
    
    def select_chapter(self, chapter_number):
        # Select a chapter within the current book
        if self.current_book is not None:
            self.current_chapter = chapter_number
            print(f"Selected chapter: {chapter_number}")
        else:
            print("Select a book first.")
    
    def display_chapter(self):
        # Display all verses in the current chapter
        if self.current_book is not None and self.current_chapter is not None:
            verses = [verse for verse in self.data['verses'] if verse['book'] == self.current_book and verse['chapter'] == self.current_chapter]
            for verse in verses:
                print(f"{verse['chapter']}:{verse['verse']} {verse['text']}")
        else:
            print("Select a book and chapter first.")
    
    def search(self, keyword):
        # Search for a keyword in all verses and display matching verses
        results = [verse for verse in self.data['verses'] if keyword.lower() in verse['text'].lower()]
        for result in results:
            print(f"{result['book_name']} {result['chapter']}:{result['verse']} {result['text']}")
    
    def add_bookmark(self, book_name, chapter, verse):
        # Add a bookmark to a specific verse
        if book_name not in self.bookmarks:
            self.bookmarks[book_name] = []
        self.bookmarks[book_name].append((chapter, verse))
        print(f"Bookmark added: {book_name} {chapter}:{verse}")
    
    def list_bookmarks(self):
        # List all bookmarks
        for book_name, chapters in self.bookmarks.items():
            for chapter, verse in chapters:
                print(f"{book_name} {chapter}:{verse}")
    
    def add_note(self, book_name, chapter, verse, text):
        # Add a note to a specific verse
        if book_name not in self.notes:
            self.notes[book_name] = []
        self.notes[book_name].append({'chapter': chapter, 'verse': verse, 'text': text})
        print(f"Note added: {book_name} {chapter}:{verse} - {text}")
    
    def list_notes(self):
        # List all notes
        for book_name, notes in self.notes.items():
            for note in notes:
                print(f"{book_name} {note['chapter']}:{note['verse']} - {note['text']}")
    
    def run(self):
        # Main loop to run the app
        while True:
            command = input("Enter command (info, books, book, chapter, display, search, bookmark, bookmarks, note, notes, quit): ")
            if command == "info":
                self.display_info()
            elif command == "books":
                self.list_books()
            elif command.startswith("book "):
                _, book_name = command.split(" ", 1)
                self.select_book(book_name)
            elif command.startswith("chapter "):
                _, chapter_number = command.split(" ", 1)
                self.select_chapter(int(chapter_number))
            elif command == "display":
                self.display_chapter()
            elif command.startswith("search "):
                _, keyword = command.split(" ", 1)
                self.search(keyword)
            elif command.startswith("bookmark "):
                _, book_name, chapter, verse = command.split(" ")
                self.add_bookmark(book_name, int(chapter), int(verse))
            elif command == "bookmarks":
                self.list_bookmarks()
            elif command.startswith("note "):
                _, book_name, chapter, verse, text = command.split(" ", 4)
                self.add_note(book_name, int(chapter), int(verse), text)
            elif command == "notes":
                self.list_notes()
            elif command == "quit":
                break
            else:
                print("Unknown command.")

if __name__ == "__main__":
    file_path = "reformatted_bible.json"
    app = BibleApp(file_path)
    app.run()
