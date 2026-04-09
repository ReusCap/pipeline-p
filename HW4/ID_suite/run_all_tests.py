import unittest
from HW4.ID_suite.test_length import TestLength
from HW4.ID_suite.test_format import TestFormat

# 1. 테스트 스위트 생성
suite = unittest.TestSuite()

# 2. 테스트 클래스 전체 추가
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestLength))
suite.addTest(loader.loadTestsFromTestCase(TestFormat))

# 3. 테스트 실행기 생성 및 실행
runner = unittest.TextTestRunner()
runner.run(suite)