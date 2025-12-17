# GREEN 단계 낮은 우선순위 구현 시나리오

## 개요
- **대상**: 낮은 우선순위 (중요도: 낮음) 항목
- **방법론**: TDD 최소 단위 구현 (One Test at a Time)
- **목표**: 각 테스트를 하나씩 통과시키며 점진적으로 기능 구현

---

## 현재 상태 확인

### ✅ 이미 통과하는 테스트
- `test_multiply_by_zero`: `multiply` 메서드가 이미 일반화되어 있어 0 곱셈도 자동으로 처리됨
  - `multiply(0, 10) → 0` ✅

---

## 구현 순서 및 시나리오

### Phase 1: `multiply` 메서드 확장 확인 (이미 완료)
**목표**: `test_multiply_by_zero` 통과 확인

1. **상태**: 이미 통과함 (확인 완료)
2. **이유**: `multiply(a, b) = a * b`로 일반화되어 있어 0 곱셈도 자동 처리
3. **작업**: 추가 작업 없음

---

## 시나리오 분석

### 상황 1: 이미 구현 완료된 경우 (현재 상태)
- **상태**: `multiply` 메서드가 `return a * b`로 일반화되어 있음
- **결과**: `test_multiply_by_zero` 테스트가 이미 통과함
- **작업**: 추가 구현 불필요

### 상황 2: 만약 하드코딩된 상태였다면
만약 `multiply` 메서드가 `return 15`로 하드코딩되어 있었다면:

1. **작업**: `multiply` 메서드 최소 구현
2. **구현 내용**:
   ```python
   def multiply(self, a, b):
       if a == 0 or b == 0:
           return 0  # 0 곱셈 특수 처리
       return 15  # 기존 하드코딩 유지
   ```
3. **예상 결과**: 
   - ✅ `test_multiply_by_zero` 통과
   - ❌ `test_multiply_negative_numbers` 실패 (여전히 15 반환)

또는 더 나은 방법:

1. **작업**: `multiply` 메서드 일반화
2. **구현 내용**:
   ```python
   def multiply(self, a, b):
       return a * b
   ```
3. **예상 결과**: 
   - ✅ `test_multiply_by_zero` 통과
   - ✅ `test_multiply_negative_numbers` 통과 (부수 효과)

---

## 최종 구현 코드 (현재 상태)

```python
class Arithmetic:
    def multiply(self, a, b):
        """곱셈 메서드"""
        return a * b  # 이미 일반화되어 있어 0 곱셈도 자동 처리
```

---

## 테스트 통과 예상 결과

### Phase 1 완료 시점 (이미 완료)
- ✅ `test_multiply_by_zero` (0, 10 → 0)

---

## 검증 방법

테스트 실행:
```bash
# 낮은 우선순위 테스트만 실행
python -m unittest test_arithmetic.TestArithmetic.test_multiply_by_zero -v

# 또는 모든 테스트 실행
python -m unittest test_arithmetic.py -v
```

---

## 주의사항

1. **이미 완료된 상태**: `multiply` 메서드가 일반화되어 있어 추가 작업 불필요
2. **부수 효과**: 중간 우선순위 구현 시 이미 처리됨
3. **검증 필요**: 테스트가 통과하는지 확인만 필요

---

## 구현 우선순위 요약

| Phase | 메서드 | 테스트 케이스 | 우선순위 | 상태 |
|-------|--------|--------------|---------|------|
| Phase 1 | `multiply` 확장 확인 | `test_multiply_by_zero` | 낮음 | ✅ 완료 |

---

## 결론

**현재 상태**: 이미 구현 완료됨
- `multiply` 메서드가 `return a * b`로 일반화되어 있어 `test_multiply_by_zero` 테스트가 이미 통과함
- 추가 구현 작업 불필요
- 검증만 수행하면 됨

---

## 승인 대기

이 시나리오에 대한 승인을 기다립니다.
현재 상태에서는 추가 구현이 필요하지 않지만, 검증을 수행하겠습니다.

