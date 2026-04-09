import unittest
from HW4.ID_suite.test_length import TestLength
from HW4.ID_suite.test_format import TestFormat

# 1. 테스트 스위트 생성
suite = unittest.TestSuite()

# 2. 특정 테스트 메서드만 추가 (이름 문자열로 지정)
suite.addTest(TestLength('test_length_success'))
suite.addTest(TestFormat('test_format_success'))

# 3. 실행기 생성 및 실행
runner = unittest.TextTestRunner()
runner.run(suite)