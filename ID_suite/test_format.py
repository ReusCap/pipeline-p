import unittest
from id_validator import IDValidator

class TestFormat(unittest.TestCase):
    def test_format_success(self):
        self.assertEqual(IDValidator().is_valid_format("python123"), True)

    def test_format_only_alpha(self):
        self.assertEqual(IDValidator().is_valid_format("purealpha"), False)