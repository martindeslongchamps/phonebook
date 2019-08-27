import inject

from sources.contact import Contact
from sources.directory import Directory
from sources.phone.phone_number_validator import PhoneNumberValidator
from sources.phonebook import Phonebook


# Create an optional configuration.
def configure_container(container):
    container.bind(PhoneNumberValidator, PhoneNumberValidator("test"))


# Configure a shared injector.
inject.configure(configure_container)

d = inject.instance(Directory)
ph = inject.instance(Phonebook)
ph2 = inject.instance(Phonebook)
ph.set_number("514.346.2980")
ph2.set_number("514.346.2981")
d.add_phone_book(ph)
d.add_phone_book(ph2)

print(d.phonebooks[0].number)

c1 = Contact(first_name="Martin", last_name="Deslongchamps")
c2 = Contact(first_name="Lucien", last_name="")

d.add_contact(c1)
d.add_contact(c2)
d.show_contacts()
