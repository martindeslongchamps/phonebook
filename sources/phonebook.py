import inject

from sources.phone.phone_number_validator import PhoneNumberValidator


class Phonebook:

    @inject.autoparams()
    def __init__(self, validator: PhoneNumberValidator):
        self.validator = validator
        self.number = None

    def set_number(self, number: str):
        if self.validator.validate(number):
            self.number = number
        else:
            self.number = None

