# test_id.py
import unittest
from HW4.ID.id import IDValidator

class TestIDValidator(unittest.TestCase):

    def setUp(self):
        print(">> setUp 실행됨")
        # 모든 테스트 전에 새로운 IDValidator 객체 생성
        self.validator = IDValidator()

    def tearDown(self):
        print("<< tearDown 실행됨")

    def test_valid_id(self):
        # 성공 케이스
        self.assertEqual(self.validator.is_valid("python123"), True)

    def test_short_id(self):
        # 실패 케이스 (8자 미만)
        self.assertEqual(self.validator.is_valid("py12"), False)

    def test_only_alpha_id(self):
        # 실패 케이스 (숫자 없음)
        self.assertEqual(self.validator.is_valid("purealphabet"), False)

if __name__ == '__main__':
    unittest.main()