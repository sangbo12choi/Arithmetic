# GREEN 단계 중간 우선순위 구현 시나리오

## 개요
- **대상**: 중간 우선순위 (중요도: 보통) 항목
- **방법론**: TDD 최소 단위 구현 (One Test at a Time)
- **목표**: 각 테스트를 하나씩 통과시키며 점진적으로 기능 구현

---

## 현재 상태 확인

### ✅ 이미 통과하는 테스트
- `test_add_negative_numbers`: `add` 메서드가 이미 일반화되어 있어 음수 덧셈도 자동으로 처리됨
  - `add(-1, -10) → -11` ✅

### ❌ 구현 필요한 테스트
- `test_multiply_negative_numbers`: `multiply` 메서드 미구현
- `test_divide_quotient`: `quotient` 메서드 미구현

---

## 구현 순서 및 시나리오

### Phase 1: `add` 메서드 확장 확인 (이미 완료)
**목표**: `test_add_negative_numbers` 통과 확인

1. **상태**: 이미 통과함 (확인 완료)
2. **이유**: `add(a, b) = a + b`로 일반화되어 있어 음수도 자동 처리
3. **작업**: 추가 작업 없음

---

### Phase 2: `multiply(a, b)` 메서드 - 첫 번째 테스트 통과
**목표**: `test_multiply_negative_numbers` 통과

1. **작업**: `multiply` 메서드 최소 구현
2. **구현 내용**:
   ```python
   def multiply(self, a, b):
       return 15  # 하드코딩된 값 (-5 * -3 = 15)
   ```
3. **예상 결과**: 
   - ✅ `test_multiply_negative_numbers` 통과
   - ❌ `test_multiply_by_zero` 실패 (0 * 10 = 0 기대, 15 반환)

---

### Phase 3: `multiply(a, b)` 메서드 - 일반화
**목표**: `test_multiply_by_zero` 통과 (낮은 우선순위이지만 함께 처리)

1. **작업**: `multiply` 메서드 일반화
2. **구현 내용**:
   ```python
   def multiply(self, a, b):
       return a * b
   ```
3. **예상 결과**: 
   - ✅ `test_multiply_negative_numbers` 통과
   - ✅ `test_multiply_by_zero` 통과 (부수 효과)

---

### Phase 4: `quotient(a, b)` 메서드 구현
**목표**: `test_divide_quotient` 통과

1. **작업**: `quotient` 메서드 구현 (소수점 나눗셈)
2. **구현 내용**:
   ```python
   def quotient(self, a, b):
       return 2.5  # 하드코딩된 값 (5 / 2 = 2.5)
   ```
3. **예상 결과**: 
   - ✅ `test_divide_quotient` 통과
   - ⚠️ 일반화 필요 여부: 현재는 하드코딩이지만, 실제로는 일반화가 필요할 수 있음

---

### Phase 5: `quotient(a, b)` 메서드 - 일반화 (선택사항)
**목표**: `quotient` 메서드를 일반화하여 모든 경우 처리

1. **작업**: `quotient` 메서드 일반화
2. **구현 내용**:
   ```python
   def quotient(self, a, b):
       return a / b  # 소수점 나눗셈
   ```
3. **예상 결과**: 
   - ✅ `test_divide_quotient` 통과
   - ⚠️ 0으로 나누기 예외 처리: 현재 테스트에는 없지만, 안전성을 위해 추가 고려 가능

---

## 최종 구현 코드 예상

```python
class Arithmetic:
    def add(self, a, b):
        """덧셈 메서드"""
        return a + b
    
    def subtract(self, a, b):
        """뺄셈 메서드"""
        return a - b
    
    def multiply(self, a, b):
        """곱셈 메서드"""
        return a * b
    
    def divide(self, a, b):
        """정수 나눗셈 메서드"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def quotient(self, a, b):
        """소수점 나눗셈 메서드"""
        return a / b
```

---

## 테스트 통과 예상 결과

### Phase 1 완료 시점 (이미 완료)
- ✅ `test_add_negative_numbers` (-1, -10 → -11)

### Phase 3 완료 시점
- ✅ `test_multiply_negative_numbers` (-5, -3 → 15)
- ✅ `test_multiply_by_zero` (0, 10 → 0) [부수 효과]

### Phase 4 또는 Phase 5 완료 시점
- ✅ `test_divide_quotient` (5, 2 → 2.5)

---

## 검증 방법

각 Phase 완료 후 다음 명령어로 테스트 실행:
```bash
# 중간 우선순위 테스트만 실행
python -m unittest test_arithmetic.TestArithmetic.test_add_negative_numbers test_arithmetic.TestArithmetic.test_multiply_negative_numbers test_arithmetic.TestArithmetic.test_divide_quotient -v

# 또는 모든 테스트 실행
python -m unittest test_arithmetic.py -v
```

---

## 주의사항

1. **최소 단위 원칙**: 각 Phase에서 하나의 테스트만 통과시키는 데 집중
2. **하드코딩 허용**: Phase 2, Phase 4처럼 하드코딩된 값도 초기 단계에서는 허용
3. **점진적 개선**: Phase 3, Phase 5에서 일반화하여 모든 경우 처리
4. **부수 효과**: `multiply` 일반화 시 낮은 우선순위 테스트도 자동 통과

---

## 구현 우선순위 요약

| Phase | 메서드 | 테스트 케이스 | 우선순위 | 상태 |
|-------|--------|--------------|---------|------|
| Phase 1 | `add` 확장 | `test_add_negative_numbers` | 보통 | ✅ 완료 |
| Phase 2 | `multiply` 최소 | `test_multiply_negative_numbers` | 보통 | 대기 |
| Phase 3 | `multiply` 일반화 | `test_multiply_by_zero` | 낮음 (부수) | 대기 |
| Phase 4 | `quotient` 최소 | `test_divide_quotient` | 보통 | 대기 |
| Phase 5 | `quotient` 일반화 | - | 선택사항 | 대기 |

---

## 승인 대기

이 시나리오에 대한 승인을 기다립니다.
승인 후 위 순서대로 구현을 진행하겠습니다.

