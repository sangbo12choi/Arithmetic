"""
계산기 서비스 모듈
연산자 처리 및 계산 조율을 담당하는 서비스 계층
"""

from arithmetic import Arithmetic
from operator_mapper import OperatorMapper


class CalculatorService:
    """
    계산기 서비스 클래스
    연산자 문자열을 Arithmetic 메서드로 매핑하고 계산을 수행
    """
    
    def __init__(self, arithmetic: Arithmetic = None):
        """
        CalculatorService 초기화
        
        Args:
            arithmetic: Arithmetic 인스턴스 (None이면 새로 생성)
        """
        self._arithmetic = arithmetic if arithmetic is not None else Arithmetic()
        self._operator_strategies = self._build_operator_strategies()
    
    def _build_operator_strategies(self) -> dict:
        """
        연산자별 Strategy 딕셔너리 생성
        Strategy 패턴을 사용하여 OCP 원칙 준수
        
        Returns:
            연산자 문자열을 Arithmetic 메서드로 매핑하는 딕셔너리
        """
        return {
            '+': self._arithmetic.add,
            '-': self._arithmetic.subtract,
            '*': self._arithmetic.multiply,
            '/': self._arithmetic.quotient,
            '//': self._arithmetic.divide,
            '%': self._arithmetic.modulo
        }
    
    def calculate(self, a: int, operator: str, b: int):
        """
        연산을 수행하는 메서드
        
        Args:
            a: 첫 번째 피연산자
            operator: 연산자 문자열 ('+', '-', '*', '/', '//', '%')
            b: 두 번째 피연산자
            
        Returns:
            계산 결과
            
        Raises:
            ValueError: 지원하지 않는 연산자인 경우
            ArithmeticError: 0으로 나누기 등의 산술 오류
        """
        if operator not in self._operator_strategies:
            raise ValueError(f"지원하지 않는 연산자: {operator}")
        
        strategy = self._operator_strategies[operator]
        return strategy(a, b)
    
    def format_operation(self, a: int, operator: str, b: int, use_gui_display: bool = False) -> str:
        """
        연산식을 문자열로 포맷팅
        
        Args:
            a: 첫 번째 피연산자
            operator: 연산자 문자열
            b: 두 번째 피연산자
            use_gui_display: GUI 표시 형식 사용 여부
            
        Returns:
            포맷팅된 연산식 문자열
        """
        return OperatorMapper.format_operation(a, operator, b, use_gui_display)
    
    def get_valid_operators(self) -> list[str]:
        """
        지원하는 모든 연산자 목록 반환
        
        Returns:
            지원하는 연산자 문자열 리스트
        """
        return OperatorMapper.get_valid_operators()

