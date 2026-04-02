# login.py
class AuthService:
    def verify_credentials(self, username: str, password: str) -> bool:
        raise NotImplementedError("실제 서비스 구현 필요")

class LoginManager:
    def __init__(self, auth_service: AuthService):
        self.auth_service = auth_service

    def login(self, username: str, password: str) -> str:
        if self.auth_service.verify_credentials(username, password):
            # 실제 서비스라면 여기서 JWT 혹은 세션 토큰을 생성한다.
            return f"token-{username}"
        else:
            raise ValueError("Invalid credentials")
