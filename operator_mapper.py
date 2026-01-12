"""
연산자 매핑 유틸리티 모듈
연산자 문자열을 표시 형식으로 변환하는 역할
"""


class OperatorMapper:
    """연산자 표시 문자열 매핑 클래스"""
    
    # 연산자 표시 매핑 딕셔너리
    DISPLAY_MAP = {
        '+': '+',
        '-': '-',
        '*': '×',
        '/': '÷',
        '//': '/',
        '%': '%',
        'sqrt': '√',
        'log': 'ln',
        'log10': 'log'
    }
    
    # 콘솔 출력용 매핑 (일부 연산자는 다르게 표시)
    CONSOLE_DISPLAY_MAP = {
        '+': '+',
        '-': '-',
        '*': '*',
        '/': '/',
        '//': '/',
        '%': '%',
        'sqrt': 'sqrt',
        'log': 'log',
        'log10': 'log10'
    }
    
    @classmethod
    def to_display(cls, operator: str) -> str:
        """
        연산자를 표시용 문자열로 변환
        
        Args:
            operator: 연산자 문자열 ('+', '-', '*', '/', '//', '%')
            
        Returns:
            표시용 연산자 문자열
            
        Raises:
            ValueError: 지원하지 않는 연산자인 경우
        """
        if operator not in cls.DISPLAY_MAP:
            raise ValueError(f"지원하지 않는 연산자: {operator}")
        return cls.DISPLAY_MAP[operator]
    
    @classmethod
    def to_console_display(cls, operator: str) -> str:
        """
        연산자를 콘솔 출력용 문자열로 변환
        
        Args:
            operator: 연산자 문자열
            
        Returns:
            콘솔 출력용 연산자 문자열
        """
        return cls.CONSOLE_DISPLAY_MAP.get(operator, operator)
    
    @classmethod
    def format_operation(cls, a, operator: str, b=None, use_gui_display: bool = False) -> str:
        """
        연산식을 문자열로 포맷팅
        
        Args:
            a: 첫 번째 피연산자 (단일 인자 연산의 경우 유일한 피연산자)
            operator: 연산자 문자열
            b: 두 번째 피연산자 (이항 연산의 경우 필요, None이면 단일 인자 연산)
            use_gui_display: GUI 표시 형식 사용 여부
            
        Returns:
            포맷팅된 연산식 문자열
        """
        # 단일 인자 연산 처리
        unary_operators = ['sqrt', 'log', 'log10']
        if operator in unary_operators:
            if use_gui_display:
                op_display = cls.to_display(operator)
            else:
                op_display = cls.to_console_display(operator)
            return f"{op_display}({a})"
        
        # 이항 연산 처리
        if use_gui_display:
            op_display = cls.to_display(operator)
        else:
            op_display = cls.to_console_display(operator)
        return f"{a}{op_display}{b}"
    
    @classmethod
    def get_valid_operators(cls) -> list[str]:
        """
        지원하는 모든 연산자 목록 반환
        
        Returns:
            지원하는 연산자 문자열 리스트
        """
        return list(cls.DISPLAY_MAP.keys())

