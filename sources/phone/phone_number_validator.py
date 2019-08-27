class PhoneNumberValidator:

    def __init__(self, name: str):
        self.name = name

    def validate(self, number: str):
        print(self.name)
        print(self.__hash__())
        if len(number) > 6:
            return True
        return False
