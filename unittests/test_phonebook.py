import unittest

from mock import Mock

from sources.phone.phone_number_validator import PhoneNumberValidator
from sources.phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        self.mock_validator = Mock(PhoneNumberValidator)
        self.sut = Phonebook(self.mock_validator)

    def test_create(self):
        self.assertIsNotNone(self.sut)
