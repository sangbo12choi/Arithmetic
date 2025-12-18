"""
간단한 사칙연산 콘솔 프로그램
TC-CMM-001 / TC-AO-001
사용자 입력을 받아 사칙연산을 수행하는 콘솔 프로그램

리팩토링: CalculatorView 인터페이스를 사용하도록 개선
"""

from console_calculator_view import ConsoleCalculatorView


def main():
    """메인 함수"""
    view = ConsoleCalculatorView()
    view.run()


if __name__ == '__main__':
    main()

