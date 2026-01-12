"""
사칙연산 모듈
TC-CMM-001 / TC-AO-001
TDD GREEN 단계: 테스트를 통과하는 최소한의 코드 작성
"""


class Arithmetic:
    """사칙연산 클래스"""
    
    def add(self, a, b):
        """덧셈 메서드"""
        return a + b
    
    def subtract(self, a, b):
        """뺄셈 메서드"""
        return a - b
    
    def divide(self, a, b):
        """정수 나눗셈 메서드"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a // b
    
    def multiply(self, a, b):
        """곱셈 메서드"""
        return a * b
    
    def quotient(self, a, b):
        """소수점 나눗셈 메서드"""
        return a / b
    
    def modulo(self, a, b):
        """나머지 연산 메서드"""
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a % b
    
    def sqrt(self, a):
        """제곱근 계산 메서드"""
        import math
        if a < 0:
            raise ArithmeticError("Cannot calculate square root of negative number")
        return math.sqrt(a)
    
    def log(self, a):
        """자연 로그 계산 메서드 (밑이 e)"""
        import math
        if a <= 0:
            raise ArithmeticError("Cannot calculate logarithm of non-positive number")
        return math.log(a)
    
    def log10(self, a):
        """상용 로그 계산 메서드 (밑이 10)"""
        import math
        if a <= 0:
            raise ArithmeticError("Cannot calculate logarithm of non-positive number")
        return math.log10(a)


if __name__ == '__main__':
    """메인 실행 블록: 모듈 실행 시 예제 결과 출력"""
    calc = Arithmetic()
    
    print("=" * 50)
    print("사칙연산 모듈 실행 예제")
    print("=" * 50)
    print()
    
    # 덧셈 예제
    print("[덧셈 연산]")
    print(f"  add(1, 10) = {calc.add(1, 10)}")
    print(f"  add(0, 1) = {calc.add(0, 1)}")
    print(f"  add(-1, -10) = {calc.add(-1, -10)}")
    print()
    
    # 뺄셈 예제
    print("[뺄셈 연산]")
    print(f"  subtract(5, 2) = {calc.subtract(5, 2)}")
    print()
    
    # 곱셈 예제
    print("[곱셈 연산]")
    print(f"  multiply(-5, -3) = {calc.multiply(-5, -3)}")
    print(f"  multiply(0, 10) = {calc.multiply(0, 10)}")
    print()
    
    # 나눗셈 예제
    print("[나눗셈 연산]")
    print(f"  divide(5, 2) = {calc.divide(5, 2)} (정수 나눗셈)")
    print(f"  divide(-10, 2) = {calc.divide(-10, 2)}")
    print(f"  quotient(5, 2) = {calc.quotient(5, 2)} (소수점 나눗셈)")
    print()
    
    # 예외 처리 예제
    print("[예외 처리]")
    try:
        calc.divide(0, 0)
    except ArithmeticError as e:
        print(f"  divide(0, 0) -> ArithmeticError: {e}")
    print()
    
    print("=" * 50)
    print("모든 연산이 정상적으로 실행되었습니다!")
    print("=" * 50)

