from sources.contact import Contact
from sources.phonebook import Phonebook


class Directory:

    def __init__(self):
        self.phonebooks = []
        self.contacts = []

    def add_phone_book(self, book: Phonebook):
        self.phonebooks.append(book)

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def show_contacts(self):
        for contact in self.contacts:
            contact.show_me()