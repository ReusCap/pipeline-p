# id.py
class IDValidator:
    def is_valid(self, user_id):
        # 1. 8글자 이상인지 확인
        if len(user_id) < 8:
            return False
        
        # 2. 영어와 숫자가 둘 다 포함되어 있는지 확인 (기본 함수 활용)
        has_alpha = any(c.isalpha() for c in user_id)
        has_digit = any(c.isdigit() for c in user_id)
        
        return has_alpha and has_digit