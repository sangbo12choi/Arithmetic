# Arithmetic Operations - 사칙연산 모듈

## 프로젝트 개요

사칙연산(덧셈, 뺄셈, 곱셈, 나눗셈)의 정확도를 검증하는 공통 모듈입니다.  
TDD(Test-Driven Development) 방식 중 RED-GREEN-REFACTOR 사이클을 따라 개발됩니다.

## 테스트 정보

- **테스트 ID**: TC-CMM-001 (Common Module) / TC-AO-001 (Arithmetic Operations)
- **테스트 목적**: 사칙연산 정확도 테스트
- **테스트 범위**: 공통 모듈
- **작성일**: 2020-09-01
- **버전**: v1.0

## 테스트 환경

- **언어**: Python
- **IDE**: PyCharm
- **운영 체제**: Windows 10

## 테스트 케이스

### 기본 연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | 성공 |
| 덧셈 | 0 + 1 | 1 | 중요 | 성공 |
| 덧셈 | -1 + (-10) | -11 | 보통 | 성공 |
| 뺄셈 | 5 - 2 | 3 | 중요 | 성공 |
| 곱셈 | -5 * -3 | 15 | 보통 | 성공 |
| 곱셈 | 0 * 10 | 0 | 낮음 | 성공 |
| 정수 나눗셈 | 5 / 2 | 2 | 중요 | 성공 |
| 소수점 나눗셈 | 5 ÷ 2 (quotient) | 2.5 | 보통 | 성공 |
| 나눗셈 | -10 / 2 | -5 | 중요 | 성공 |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|--------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ArithmeticException | 중요 | 성공 |

## 개발 방법론: TDD (RED-GREEN-REFACTOR)

### 1. RED 단계 -> 진행중
- 실패하는 테스트 케이스를 먼저 작성합니다.
- 테스트가 실패하는 것을 확인합니다.

### 2. GREEN 단계
- 테스트를 통과하는 최소한의 코드를 작성합니다.
- 모든 테스트 케이스가 통과하는지 확인합니다.

#### GREEN 단계 구현 목록

##### 높은 우선순위 (중요도: 중요) 🔴
1. **`add(a, b)` 메서드 구현**
   - 양수 덧셈: `add(1, 10) → 11`
   - 0과 양수 덧셈: `add(0, 1) → 1`
   - 테스트 케이스: `test_add_positive_numbers`, `test_add_zero_and_positive`

2. **`subtract(a, b)` 메서드 구현**
   - 양수 뺄셈: `subtract(5, 2) → 3`
   - 테스트 케이스: `test_subtract_positive_numbers`

3. **`divide(a, b)` 메서드 구현**
   - 정수 나눗셈: `divide(5, 2) → 2` (정수 결과)
   - 음수/양수 나눗셈: `divide(-10, 2) → -5`
   - 0으로 나누기 예외 처리: `divide(0, 0) → ArithmeticError` 발생
   - 테스트 케이스: `test_divide_integer`, `test_divide_negative_by_positive`, `test_divide_by_zero`

##### 중간 우선순위 (중요도: 보통) 🟡
4. **`add(a, b)` 메서드 확장**
   - 음수 덧셈: `add(-1, -10) → -11`
   - 테스트 케이스: `test_add_negative_numbers`

5. **`multiply(a, b)` 메서드 구현**
   - 음수 곱셈: `multiply(-5, -3) → 15`
   - 테스트 케이스: `test_multiply_negative_numbers`

6. **`quotient(a, b)` 메서드 구현**
   - 소수점 나눗셈: `quotient(5, 2) → 2.5`
   - 테스트 케이스: `test_divide_quotient`

##### 낮은 우선순위 (중요도: 낮음) 🟢
7. **`multiply(a, b)` 메서드 확장**
   - 0 곱셈: `multiply(0, 10) → 0`
   - 테스트 케이스: `test_multiply_by_zero`

#### 구현 체크리스트
- [x] `arithmetic.py` 모듈 생성
- [x] `Arithmetic` 클래스 구현
- [x] 높은 우선순위 메서드 구현 (1-3)
- [x] 중간 우선순위 메서드 구현 (4-6)
- [x] 낮은 우선순위 메서드 구현 (7)
- [x] 모든 테스트 케이스 통과 확인 (10/10)
- [x] 예외 처리 검증 (`ArithmeticError`)

### 3. REFACTOR 단계
- 코드를 개선하고 리팩토링합니다.
- 테스트가 여전히 통과하는지 확인합니다.

## 전제 조건

- Python이 설치되어 있어야 합니다.
- 프로그램은 오류 없이 성공적으로 실행되어야 합니다.
- 모든 종속성을 올바르게 설치하고 구성해야 합니다.

## 성공/실패 기준

- **성공**: 모든 테스트 사례가 예상한 결과를 생성합니다.
- **실패**: 테스트 케이스가 예상한 결과를 생성하지 않습니다.

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── arithmetic.py          # 사칙연산 모듈 (구현 예정)
├── test_arithmetic.py     # 테스트 파일 (구현 예정)
└── requirements.txt       # 종속성 파일 (필요시)
```

## 실행 방법

### 테스트 실행

```bash
# pytest를 사용하는 경우
pytest test_arithmetic.py -v

# unittest를 사용하는 경우
python -m unittest test_arithmetic.py -v
```

## 특별 절차

- 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
- 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

## 작성자 정보

- **작성자**: 홍길동
- **승인자**: 박문수
- **테스트 조직**: 개발팀

