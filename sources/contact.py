import inject

from sources.contact_validator import ContactValidator


class Contact:
    @inject.autoparams('contact_validator')
    def __init__(self, first_name: str, last_name: str, contact_validator: ContactValidator):
        self.contact_validator = contact_validator
        self.last_name = last_name
        self.first_name = first_name

    def show_me(self):
        if self.contact_validator.validate(self.first_name, self.last_name):
            print(f"My name is {self.first_name} {self.last_name}")
        else:
            print("This contact is invalid.")
