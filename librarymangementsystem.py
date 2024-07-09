import tkinter as tk

class Book:
    def __init__(self):
        self.verses = {}

    def add_verse(self, verse_number, text):
        self.verses[verse_number] = text

    def get_verse(self, verse_number):
        return self.verses.get(verse_number, "Verse not found")

# Create a book instance and add verses
my_book = Book()
my_book.add_verse(1, "In the beginning God created the heavens and the earth.")
my_book.add_verse(2, "The earth was formless and empty, and darkness covered the deep waters.")

# Create the main window
window = tk.Tk()
window.title("Book Verse Viewer")

# Create GUI elements
verse_number_label = tk.Label(window, text="Verse Number:")
verse_number_label.pack()

verse_number_entry = tk.Entry(window)
verse_number_entry.pack()

verse_text_label = tk.Label(window, text="", wraplength=400)
verse_text_label.pack()

def show_verse():
    verse_number = int(verse_number_entry.get())
    verse_text = my_book.get_verse(verse_number)
    verse_text_label.config(text=verse_text)

show_verse_button = tk.Button(window, text="Show Verse", command=show_verse)
show_verse_button.pack()

# Run the GUI main loop
window.mainloop()
