import unittest

from sources.directory import Directory


class TestDirectory(unittest.TestCase):

    def setUp(self):
        self.sut = Directory()

    def test_create(self):
        self.assertIsNotNone(self.sut)
