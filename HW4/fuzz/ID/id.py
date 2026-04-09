# id.py
class IDValidator:
    def is_valid(self, user_id: str) -> bool:
        # if not isinstance(user_id, str):
        #     return False
            
        if len(user_id) < 8:
            return False
        
        has_alpha = any(c.isalpha() for c in user_id)
        has_digit = any(c.isdigit() for c in user_id)
        
        return has_alpha and has_digit