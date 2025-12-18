# PyQt GUI 리팩토링 계획서

## 1. 코드 스멜 분석

### 발견된 문제점

#### 1.1 코드 중복
- `format_operation()`과 `format_operation_for_display()` 함수가 거의 동일한 로직을 가짐
- 연산자 매핑이 여러 곳에 하드코딩됨

#### 1.2 긴 조건문 (Long Method)
- `calculate()` 함수에 긴 if-elif 체인
- 새 연산자 추가 시 함수 수정 필요 (OCP 위반)

#### 1.3 책임 분리 부족 (SRP 위반)
- `arithmetic_console.py`가 입력 검증, 포맷팅, 계산 로직을 모두 포함
- 콘솔 특화 코드가 비즈니스 로직과 혼재

#### 1.4 일관성 부족
- 나머지 연산(%)이 `Arithmetic` 클래스를 사용하지 않음
- 다른 연산과 동일한 패턴을 따르지 않음

## 2. 정적 분석

### 2.1 순환 복잡도
- `calculate()` 함수: 복잡도 7 (높음)
- `get_operator_input()` 함수: 복잡도 3 (보통)

### 2.2 결합도
- 콘솔 프로그램이 구체적인 구현에 직접 의존
- GUI로 전환 시 대규모 수정 필요

### 2.3 응집도
- 입력/출력/계산 로직이 한 파일에 섞여있음

## 3. SOLID 원칙 분석

### 3.1 Single Responsibility Principle (SRP)
**현재 상태:**
- ❌ `arithmetic_console.py`: 입력, 검증, 포맷팅, 계산 조율이 모두 포함

**개선 방향:**
- ✅ 각 클래스가 단일 책임만 가지도록 분리
- `CalculatorService`: 계산 조율
- `OperatorMapper`: 연산자 매핑
- `CalculatorView`: UI 표시 (인터페이스)

### 3.2 Open/Closed Principle (OCP)
**현재 상태:**
- ❌ 새 연산자 추가 시 `calculate()` 함수 수정 필요
- ❌ 새 UI 추가 시 기존 코드 수정 필요

**개선 방향:**
- ✅ Strategy 패턴으로 연산자 처리
- ✅ 인터페이스 기반 UI 설계

### 3.3 Liskov Substitution Principle (LSP)
**현재 상태:**
- N/A (상속 구조 없음)

**개선 방향:**
- ✅ `CalculatorView` 인터페이스를 구현하는 모든 뷰는 상호 교체 가능

### 3.4 Interface Segregation Principle (ISP)
**현재 상태:**
- N/A (인터페이스 없음)

**개선 방향:**
- ✅ `CalculatorView` 인터페이스로 필요한 메서드만 정의

### 3.5 Dependency Inversion Principle (DIP)
**현재 상태:**
- ❌ 고수준 모듈이 구체적인 구현에 의존

**개선 방향:**
- ✅ 고수준 모듈이 `CalculatorView` 추상화에 의존
- ✅ 의존성 주입 패턴 적용

## 4. 리팩토링 단계별 계획

### Phase 1: 비즈니스 로직 계층 개선

#### 1.1 Arithmetic 클래스 확장
- `modulo(a, b)` 메서드 추가
- 모든 연산이 일관된 패턴을 따르도록 개선

#### 1.2 CalculatorService 클래스 생성
- 연산자 문자열을 Arithmetic 메서드로 매핑
- Strategy 패턴 적용으로 OCP 준수
- `calculate(a, operator, b)` 메서드 통합

#### 1.3 OperatorMapper 유틸리티 클래스 생성
- 연산자 표시 문자열 매핑
- 중복 코드 제거

**목표:**
- 코드 중복 제거
- 연산자 추가 시 확장 용이
- 테스트 가능성 향상

### Phase 2: UI 인터페이스 추상화

#### 2.1 CalculatorView 추상 클래스 생성
```python
class CalculatorView(ABC):
    @abstractmethod
    def display_input(self, text: str)
    @abstractmethod
    def display_result(self, text: str)
    @abstractmethod
    def display_error(self, message: str)
    @abstractmethod
    def get_input(self) -> tuple[int, str, int]
```

#### 2.2 ConsoleCalculatorView 구현
- 기존 `arithmetic_console.py` 로직을 뷰 클래스로 리팩토링
- `CalculatorView` 인터페이스 구현

**목표:**
- UI와 비즈니스 로직 분리
- GUI 추가 시 기존 코드 수정 최소화

### Phase 3: PyQt GUI 구현

#### 3.1 CalculatorWindow 클래스 생성
- `QMainWindow` 상속
- `CalculatorView` 인터페이스 구현

#### 3.2 UI 컴포넌트 설계
- **디스플레이 영역:**
  - 입력 표시 라인 (현재 입력 중인 수식)
  - 결과 표시 라인 (계산 결과)
  
- **키패드 영역:**
  - 숫자 버튼: 0-9
  - 연산자 버튼: +, -, ×, ÷
  - 기능 버튼: =, +/-, .
  - 레이아웃: 4x4 그리드 (이미지 참고)

#### 3.3 이벤트 처리
- 버튼 클릭 이벤트 핸들러
- 숫자 입력 처리
- 연산자 입력 처리
- 계산 실행 (= 버튼)
- 부호 변경 (+/- 버튼)

**목표:**
- 이미지와 동일한 UI 구현
- 콘솔 프로그램과 동일한 기능 제공

### Phase 4: 통합 및 테스트

#### 4.1 기존 테스트 검증
- `test_arithmetic.py` 테스트가 여전히 통과하는지 확인
- 리팩토링으로 인한 회귀 테스트

#### 4.2 GUI 테스트
- 각 버튼 동작 테스트
- 예외 상황 처리 테스트 (0으로 나누기 등)

**목표:**
- 기존 기능 유지
- 새 기능 정상 동작 확인

## 5. 최종 아키텍처

```
┌─────────────────────────────────────┐
│     Presentation Layer              │
│  ┌─────────────┐  ┌─────────────┐  │
│  │ ConsoleView │  │  GuiView    │  │
│  └──────┬──────┘  └──────┬──────┘  │
│         │                │          │
│         └────────┬───────┘          │
│                  │                  │
│         ┌────────▼────────┐         │
│         │ CalculatorView  │ (ABC)   │
│         └────────┬────────┘         │
└──────────────────┼──────────────────┘
                   │
┌──────────────────▼──────────────────┐
│      Service Layer                  │
│  ┌──────────────────────────────┐   │
│  │    CalculatorService         │   │
│  │  - calculate()               │   │
│  │  - OperatorMapper 사용       │   │
│  └──────────────┬───────────────┘   │
└─────────────────┼───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│      Domain Layer                   │
│  ┌──────────────────────────────┐   │
│  │      Arithmetic              │   │
│  │  - add()                     │   │
│  │  - subtract()                │   │
│  │  - multiply()                │   │
│  │  - divide()                  │   │
│  │  - quotient()                │   │
│  │  - modulo()                  │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
```

## 6. 구현 우선순위

1. **High Priority**: Phase 1 (비즈니스 로직 개선)
   - 코드 품질 향상
   - 테스트 가능성 향상

2. **High Priority**: Phase 2 (인터페이스 추상화)
   - GUI 추가를 위한 기반 마련

3. **High Priority**: Phase 3 (PyQt GUI 구현)
   - 사용자 요구사항 충족

4. **Medium Priority**: Phase 4 (테스트)
   - 품질 보증

## 7. 예상 효과

### 코드 품질
- 순환 복잡도 감소 (7 → 3 이하)
- 코드 중복 제거
- 유지보수성 향상

### 확장성
- 새 연산자 추가 용이 (OCP 준수)
- 새 UI 추가 용이 (DIP 준수)

### 테스트 가능성
- 각 계층별 독립적 테스트 가능
- Mock 객체를 통한 단위 테스트 용이

