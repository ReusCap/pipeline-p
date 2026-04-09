import unittest
from HW4.ID_suite.id_validator import IDValidator

class TestLength(unittest.TestCase):
    def test_length_success(self):
        self.assertEqual(IDValidator().is_valid_length("python123"), True)

    def test_length_fail(self):
        self.assertEqual(IDValidator().is_valid_length("py12"), False)