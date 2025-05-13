from abc import ABC, abstractmethod
import logging.config
from logging_config import LOGGING_CONFIG


logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('solid')
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self):
        pass
    
    @abstractmethod
    def remove_book(self):
        pass
    
    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, year):
        self.books.append(Book(title, author, year))

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            logger.debug(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(title, author, year)

    def remove_book(self, title):
        self.library.remove_book(title)
    
    def show_books(self):
        self.library.show_books()
   
def main():

    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.debug("Invalid command. Please try again.")

if __name__ == "__main__":
    main()