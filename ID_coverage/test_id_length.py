# test_id_length.py
import unittest
import id_validator

class TestIDLength(unittest.TestCase):
    def test_length(self):
        # 8자 이상 성공 테스트
        self.assertEqual(id_validator.is_valid_length("python123"), True)

if __name__ == '__main__':
    unittest.main()