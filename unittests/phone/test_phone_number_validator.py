import unittest

from sources.phone.phone_number_validator import PhoneNumberValidator


class TestPhoneNumberValidator(unittest.TestCase):

    def setUp(self):
        self.sut = PhoneNumberValidator()

    def test_create(self):
        self.assertIsNotNone(self.sut)

    def test_valid_number(self):
        self.assertTrue(self.sut.validate("514.346.2980"))

    def test_invalid_number(self):
        self.assertFalse(self.sut.validate("2980"))

