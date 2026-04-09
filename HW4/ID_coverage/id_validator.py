# id_validator.py
def is_valid_length(user_id):
    return len(user_id) >= 8

def is_valid_format(user_id):
    has_alpha = any(c.isalpha() for c in user_id)
    has_digit = any(c.isdigit() for c in user_id)
    
    # 커버리지 확인을 위해 일부러 분기 추가
    if has_alpha and has_digit:
        return True
    else:
        return False