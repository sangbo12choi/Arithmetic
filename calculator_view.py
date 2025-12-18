"""
계산기 뷰 인터페이스 모듈
UI 추상화를 위한 추상 기본 클래스
"""

from abc import ABC, abstractmethod
from typing import Tuple, Optional


class CalculatorView(ABC):
    """
    계산기 뷰 추상 클래스
    모든 계산기 UI 구현체가 따라야 하는 인터페이스
    """
    
    @abstractmethod
    def display_input(self, text: str) -> None:
        """
        입력 내용을 표시
        
        Args:
            text: 표시할 텍스트
        """
        pass
    
    @abstractmethod
    def display_result(self, text: str) -> None:
        """
        계산 결과를 표시
        
        Args:
            text: 표시할 결과 텍스트
        """
        pass
    
    @abstractmethod
    def display_error(self, message: str) -> None:
        """
        오류 메시지를 표시
        
        Args:
            message: 오류 메시지
        """
        pass
    
    @abstractmethod
    def get_input(self) -> Tuple[int, str, int]:
        """
        사용자로부터 입력을 받음
        
        Returns:
            (첫 번째 피연산자, 연산자, 두 번째 피연산자) 튜플
        """
        pass
    
    @abstractmethod
    def show_calculation_process(self, operation_str: str) -> None:
        """
        계산 과정을 표시
        
        Args:
            operation_str: 계산할 연산식 문자열
        """
        pass

