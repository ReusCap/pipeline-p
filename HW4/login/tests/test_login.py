# test_login.py
import unittest
from unittest.mock import Mock
from HW4.login.src.login import LoginManager, AuthService

class TestLoginManagerWithMock(unittest.TestCase):
    def setUp(self):
        self.mock_auth = Mock(spec=AuthService)
        self.login_manager = LoginManager(self.mock_auth)

    def test_login_success_calls_auth_service_correctly(self):
        self.mock_auth.verify_credentials.return_value = True
        username = "alice"
        password = "s3cr3t"

        token = self.login_manager.login(username, password)

        self.assertEqual(token, f"token-{username}")

        self.mock_auth.verify_credentials.assert_called_once_with(username, password)

    def test_login_failure_raises_error_and_calls_auth_once(self):
        self.mock_auth.verify_credentials.return_value = False
        username = "bob"
        password = "wrong"

        with self.assertRaises(ValueError) as cm:
            self.login_manager.login(username, password)

        self.assertEqual(str(cm.exception), "Invalid credentials")

        self.mock_auth.verify_credentials.assert_called_once_with(username, password)

if __name__ == "__main__":
    unittest.main()
