# test_divide_negative_by_positive 테스트 결과

## 테스트 정보
- **테스트 메서드**: `test_divide_negative_by_positive`
- **테스트 목적**: 음수를 양수로 나누기 테스트 (-10 / 2 = -5)
- **테스트 일시**: 2024년

## 테스트 실행 명령어
```bash
python -m unittest test_arithmetic.TestArithmetic.test_divide_negative_by_positive -v
```

## 테스트 결과

### 실행 결과
```
ERROR: test_arithmetic (unittest.loader._FailedTest) ... ERROR

======================================================================
ERROR: test_arithmetic (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: test_arithmetic
Traceback (most recent call last):
  File "C:\Users\902_05\AppData\Local\Programs\Python\Python310\lib\unittest\loader.py", line 154, in loadTestsFromName
    module = __import__(module_name)
  File "C:\DEV\Cursor_pro\Arithmetic\test_arithmetic.py", line 8, in <module>
    from arithmetic import Arithmetic
ModuleNotFoundError: No module named 'arithmetic'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (errors=1)
```

### 실패 원인
- **에러 타입**: `ModuleNotFoundError`
- **원인**: `arithmetic` 모듈이 존재하지 않음
- **에러 위치**: `test_arithmetic.py` 8번째 줄

### 테스트 상태
- ❌ **실패**: RED 단계에서 예상된 실패
- **다음 단계**: `arithmetic.py` 모듈 구현 필요

## 테스트 케이스 상세
```python
def test_divide_negative_by_positive(self):
    """음수를 양수로 나누기 테스트: -10 / 2 = -5"""
    result = self.calc.divide(-10, 2)
    self.assertEqual(result, -5, "-10 / 2는 -5이어야 합니다")
```

### 예상 동작
- `Arithmetic` 클래스의 `divide(-10, 2)` 메서드 호출
- 반환값이 `-5`인지 확인 (음수를 양수로 나눈 결과)

### 현재 상태
- `Arithmetic` 클래스가 존재하지 않아 테스트 실행 불가
- RED 단계 목표 달성: 실패하는 테스트 확인 완료

### 테스트 케이스 요구사항
- **입력값**: -10, 2
- **예상값**: -5
- **중요도**: 중요
- **상태**: 성공 (구현 후)

### 참고사항
- 음수를 양수로 나누면 결과는 음수가 되어야 함
- 정수 나눗셈이므로 소수점은 버려야 함

