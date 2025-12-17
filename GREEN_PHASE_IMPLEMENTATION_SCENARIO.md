# GREEN 단계 최소 단위 구현 시나리오

## 개요
- **대상**: 높은 우선순위 (중요도: 중요) 항목
- **방법론**: TDD 최소 단위 구현 (One Test at a Time)
- **목표**: 각 테스트를 하나씩 통과시키며 점진적으로 기능 구현

---

## 구현 순서 및 시나리오

### Phase 1: 기본 모듈 구조 생성
**목표**: 모듈 임포트 오류 해결

1. **작업**: `arithmetic.py` 파일 생성
2. **구현 내용**:
   ```python
   class Arithmetic:
       pass
   ```
3. **예상 결과**: `ModuleNotFoundError` 해결, 모든 테스트는 여전히 실패 (메서드 없음)

---

### Phase 2: `add(a, b)` 메서드 - 첫 번째 테스트 통과
**목표**: `test_add_positive_numbers` 통과

1. **작업**: `add` 메서드 최소 구현
2. **구현 내용**:
   ```python
   def add(self, a, b):
       return 11  # 하드코딩된 값
   ```
3. **예상 결과**: 
   - ✅ `test_add_positive_numbers` 통과
   - ❌ `test_add_zero_and_positive` 실패 (0 + 1 = 1 기대, 11 반환)

---

### Phase 3: `add(a, b)` 메서드 - 두 번째 테스트 통과
**목표**: `test_add_zero_and_positive` 통과

1. **작업**: `add` 메서드 일반화
2. **구현 내용**:
   ```python
   def add(self, a, b):
       return a + b
   ```
3. **예상 결과**: 
   - ✅ `test_add_positive_numbers` 통과
   - ✅ `test_add_zero_and_positive` 통과
   - ✅ `test_add_negative_numbers` 통과 (부수 효과)

---

### Phase 4: `subtract(a, b)` 메서드 구현
**목표**: `test_subtract_positive_numbers` 통과

1. **작업**: `subtract` 메서드 구현
2. **구현 내용**:
   ```python
   def subtract(self, a, b):
       return a - b
   ```
3. **예상 결과**: 
   - ✅ `test_subtract_positive_numbers` 통과

---

### Phase 5: `divide(a, b)` 메서드 - 첫 번째 테스트 통과
**목표**: `test_divide_integer` 통과

1. **작업**: `divide` 메서드 최소 구현 (정수 나눗셈)
2. **구현 내용**:
   ```python
   def divide(self, a, b):
       return a // b  # 정수 나눗셈 (5 // 2 = 2)
   ```
3. **예상 결과**: 
   - ✅ `test_divide_integer` 통과 (5 // 2 = 2)
   - ❌ `test_divide_negative_by_positive` 실패 (-10 // 2 = -5, 통과 가능성 있음)
   - ❌ `test_divide_by_zero` 실패 (ZeroDivisionError 발생, ArithmeticError 기대)

---

### Phase 6: `divide(a, b)` 메서드 - 예외 처리 추가
**목표**: `test_divide_by_zero` 통과

1. **작업**: 0으로 나누기 예외 처리 추가
2. **구현 내용**:
   ```python
   def divide(self, a, b):
       if b == 0:
           raise ArithmeticError("Division by zero")
       return a // b
   ```
3. **예상 결과**: 
   - ✅ `test_divide_integer` 통과
   - ✅ `test_divide_by_zero` 통과 (ArithmeticError 발생)
   - ✅ `test_divide_negative_by_positive` 통과 (-10 // 2 = -5)

---

## 최종 구현 코드 예상

```python
class Arithmetic:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
```

---

## 테스트 통과 예상 결과

### Phase 3 완료 시점
- ✅ `test_add_positive_numbers` (1, 10 → 11)
- ✅ `test_add_zero_and_positive` (0, 1 → 1)
- ✅ `test_add_negative_numbers` (-1, -10 → -11) [부수 효과]

### Phase 4 완료 시점
- ✅ `test_subtract_positive_numbers` (5, 2 → 3)

### Phase 6 완료 시점
- ✅ `test_divide_integer` (5, 2 → 2)
- ✅ `test_divide_negative_by_positive` (-10, 2 → -5)
- ✅ `test_divide_by_zero` (0, 0 → ArithmeticError)

---

## 검증 방법

각 Phase 완료 후 다음 명령어로 테스트 실행:
```bash
python -m unittest test_arithmetic.py -v
```

또는 특정 테스트만 실행:
```bash
python -m unittest test_arithmetic.TestArithmetic.test_add_positive_numbers -v
```

---

## 주의사항

1. **최소 단위 원칙**: 각 Phase에서 하나의 테스트만 통과시키는 데 집중
2. **하드코딩 허용**: Phase 2처럼 하드코딩된 값도 초기 단계에서는 허용
3. **점진적 개선**: Phase 3에서 일반화하여 모든 덧셈 테스트 통과
4. **예외 처리**: Phase 6에서 예외 처리를 추가하여 안전성 확보

---

## 승인 대기

이 시나리오에 대한 승인을 기다립니다.
승인 후 위 순서대로 구현을 진행하겠습니다.

