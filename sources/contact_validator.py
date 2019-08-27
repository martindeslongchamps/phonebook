class ContactValidator:
    def __init__(self):
        pass

    def validate(self, first_name, last_name):
        if len(first_name) > 0 and len(last_name) > 0:
            return True
        return False