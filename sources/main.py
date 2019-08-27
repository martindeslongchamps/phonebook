import inject

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
ph.set_number("514.346.2980")
d.add_phone_book(ph)

print(d.phonebooks[0].number)
