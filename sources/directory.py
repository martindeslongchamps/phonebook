from sources.phonebook import Phonebook


class Directory:

    def __init__(self):
        self.phonebooks = []

    def add_phone_book(self, book: Phonebook):
        self.phonebooks.append(book)