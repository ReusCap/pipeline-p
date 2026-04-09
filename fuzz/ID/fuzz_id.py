# fuzz_id.py
from hypothesis import given, strategies as st, settings
from id import IDValidator
import pytest

# 테스트 대상 객체 생성
validator = IDValidator()

@settings(max_examples=1000)  # 1,000개의 무작위 케이스 테스트
@given(user_id=st.one_of(st.text(), st.none(), st.integers()))
def test_id_fuzzing(user_id):
    try:
        result = validator.is_valid(user_id)

        assert isinstance(result, bool)
        
        if result:
            assert len(user_id) >= 8
            assert any(c.isalpha() for c in user_id)
            assert any(c.isdigit() for c in user_id)
            
    except Exception as e:
        pytest.fail(f"Fuzzing found a crash! Input: {repr(user_id)}, Error: {e}")

if __name__ == "__main__":
    test_id_fuzzing()
    print("ID Fuzzing 완료: 특이사항 없음")