class IDValidator:
    def is_valid_length(self, user_id):
        return len(user_id) >= 8

    def is_valid_format(self, user_id):
        has_alpha = any(c.isalpha() for c in user_id)
        has_digit = any(c.isdigit() for c in user_id)
        return has_alpha and has_digit