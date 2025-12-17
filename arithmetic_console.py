"""
간단한 사칙연산 콘솔 프로그램
TC-CMM-001 / TC-AO-001
사용자 입력을 받아 사칙연산을 수행하는 콘솔 프로그램
"""

from arithmetic import Arithmetic


def get_integer_input(prompt):
    """정수값을 입력받는 함수"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("올바른 정수를 입력해주세요.")


def get_operator_input():
    """연산자를 입력받는 함수"""
    valid_operators = ['+', '-', '*', '/', '//', '%']
    while True:
        operator = input("연산자 >>")
        if operator in valid_operators:
            return operator
        print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")


def calculate(calc, a, operator, b):
    """연산을 수행하는 함수"""
    if operator == '+':
        return calc.add(a, b)
    elif operator == '-':
        return calc.subtract(a, b)
    elif operator == '*':
        return calc.multiply(a, b)
    elif operator == '/':
        return calc.quotient(a, b)
    elif operator == '//':
        return calc.divide(a, b)
    elif operator == '%':
        # 나머지 연산은 Python 내장 연산자 사용
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a % b
    else:
        raise ValueError(f"지원하지 않는 연산자: {operator}")


def format_operation(a, operator, b):
    """연산식을 문자열로 포맷팅"""
    operator_display = {
        '+': '+',
        '-': '-',
        '*': '*',
        '/': '÷',
        '//': '/',
        '%': '%'
    }
    return f"{a}{operator_display.get(operator, operator)}{b}"


def format_operation_for_display(a, operator, b):
    """결과 화면용 연산식 포맷팅"""
    operator_display = {
        '+': '+',
        '-': '-',
        '*': '*',
        '/': '/',
        '//': '/',
        '%': '%'
    }
    return f"{a}{operator_display.get(operator, operator)}{b}"


def main():
    """메인 함수"""
    calc = Arithmetic()
    
    # 입력 화면
    a = get_integer_input("첫번째 정수값>>")
    operator = get_operator_input()
    b = get_integer_input("두번째 정수값>>")
    
    # 결과 뷰 화면
    print("=" * 35)
    operation_str = format_operation_for_display(a, operator, b)
    print(f"{operation_str}을 계산합니다.")
    print("=" * 35)
    
    try:
        result = calculate(calc, a, operator, b)
        print(f"{operation_str}={result} 입니다.")
    except ArithmeticError as e:
        print(f"오류: {e}")
    except Exception as e:
        print(f"오류 발생: {e}")


if __name__ == '__main__':
    main()

