# test_id_format.py
import unittest
import HW4.ID_coverage.id_validator as id_validator

class TestIDFormat(unittest.TestCase):
    def test_format(self):
        # 형식 성공 테스트
        self.assertEqual(id_validator.is_valid_format("python123"), True)

if __name__ == '__main__':
    unittest.main()