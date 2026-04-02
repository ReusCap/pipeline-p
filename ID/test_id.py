# test_id.py
import unittest
from id import IDValidator

class TestIDValidator(unittest.TestCase):
    def test_id_check(self):
        val = IDValidator()
        
        # 성공 케이스 (영어 + 숫자 8자 이상)
        self.assertEqual(val.is_valid("python123"), True)
        # 실패 케이스 (8자 미만)
        self.assertEqual(val.is_valid("py12"), False)
        # 실패 케이스 (숫자 없음)
        self.assertEqual(val.is_valid("purealphabet"), False)

if __name__ == '__main__':
    unittest.main()