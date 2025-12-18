"""
콘솔 계산기 뷰 구현
CalculatorView 인터페이스의 콘솔 구현체
"""

from calculator_view import CalculatorView
from calculator_service import CalculatorService
from typing import Tuple


class ConsoleCalculatorView(CalculatorView):
    """콘솔 기반 계산기 뷰"""
    
    def __init__(self, calculator_service: CalculatorService = None):
        """
        ConsoleCalculatorView 초기화
        
        Args:
            calculator_service: CalculatorService 인스턴스
        """
        self._service = calculator_service if calculator_service is not None else CalculatorService()
    
    def display_input(self, text: str) -> None:
        """입력 내용을 콘솔에 표시"""
        print(text)
    
    def display_result(self, text: str) -> None:
        """계산 결과를 콘솔에 표시"""
        print(text)
    
    def display_error(self, message: str) -> None:
        """오류 메시지를 콘솔에 표시"""
        print(f"오류: {message}")
    
    def get_integer_input(self, prompt: str) -> int:
        """
        정수값을 입력받는 메서드
        
        Args:
            prompt: 입력 프롬프트
            
        Returns:
            입력받은 정수값
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("올바른 정수를 입력해주세요.")
    
    def get_operator_input(self) -> str:
        """
        연산자를 입력받는 메서드
        
        Returns:
            입력받은 연산자 문자열
        """
        valid_operators = self._service.get_valid_operators()
        while True:
            operator = input("연산자 >>")
            if operator in valid_operators:
                return operator
            print(f"올바른 연산자를 입력해주세요. ({', '.join(valid_operators)})")
    
    def get_input(self) -> Tuple[int, str, int]:
        """
        사용자로부터 입력을 받음
        
        Returns:
            (첫 번째 피연산자, 연산자, 두 번째 피연산자) 튜플
        """
        a = self.get_integer_input("첫번째 정수값>>")
        operator = self.get_operator_input()
        b = self.get_integer_input("두번째 정수값>>")
        return a, operator, b
    
    def show_calculation_process(self, operation_str: str) -> None:
        """
        계산 과정을 콘솔에 표시
        
        Args:
            operation_str: 계산할 연산식 문자열
        """
        print("=" * 35)
        print(f"{operation_str}을 계산합니다.")
        print("=" * 35)
    
    def run(self) -> None:
        """
        계산기 프로그램 실행
        메인 루프
        """
        # 입력 받기
        a, operator, b = self.get_input()
        
        # 계산 과정 표시
        operation_str = self._service.format_operation(a, operator, b, use_gui_display=False)
        self.show_calculation_process(operation_str)
        
        # 계산 수행 및 결과 표시
        try:
            result = self._service.calculate(a, operator, b)
            self.display_result(f"{operation_str}={result} 입니다.")
        except ArithmeticError as e:
            self.display_error(str(e))
        except Exception as e:
            self.display_error(f"오류 발생: {e}")

