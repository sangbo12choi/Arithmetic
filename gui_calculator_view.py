"""
PyQt 기반 GUI 계산기 뷰 구현
CalculatorView 인터페이스의 GUI 구현체
"""

import sys
from functools import partial
from typing import Tuple, Optional
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, 
    QLabel, QApplication
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from calculator_service import CalculatorService


class CalculatorWindow(QMainWindow):
    """
    PyQt 기반 계산기 윈도우
    이미지와 동일한 키패드 레이아웃 구현
    """
    
    # 계산 완료 시그널 (입력 완료를 알림)
    calculation_requested = pyqtSignal(int, str, int)
    
    def __init__(self, calculator_service: CalculatorService = None):
        """
        CalculatorWindow 초기화
        
        Args:
            calculator_service: CalculatorService 인스턴스
        """
        super().__init__()
        self._service = calculator_service if calculator_service is not None else CalculatorService()
        
        # 계산기 상태
        self._first_number: Optional[int] = None
        self._operator: Optional[str] = None
        self._second_number: Optional[int] = None
        self._current_input: str = ""
        self._waiting_for_operand: bool = True
        
        self._init_ui()
        self._connect_signals()
        
        # 초기 디스플레이 설정
        self._update_display()
    
    def _init_ui(self):
        """UI 초기화"""
        self.setWindowTitle("계산기")
        self.setFixedSize(300, 400)
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 디스플레이 영역
        display_layout = QVBoxLayout()
        
        # 입력 표시 라인
        self._input_label = QLabel("0")
        self._input_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._input_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                padding: 5px;
                font-size: 14px;
                color: #666;
            }
        """)
        self._input_label.setFixedHeight(30)
        display_layout.addWidget(self._input_label)
        
        # 결과 표시 라인
        self._result_label = QLabel("")
        self._result_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self._result_label.setFont(font)
        self._result_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        self._result_label.setFixedHeight(50)
        display_layout.addWidget(self._result_label)
        
        main_layout.addLayout(display_layout)
        
        # 키패드 영역
        keypad_layout = QGridLayout()
        keypad_layout.setSpacing(5)
        
        # 버튼 스타일
        number_button_style = """
            QPushButton {
                background-color: #2c2c2c;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #3c3c3c;
            }
            QPushButton:pressed {
                background-color: #1c1c1c;
            }
        """
        
        operator_button_style = """
            QPushButton {
                background-color: #2c2c2c;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #3c3c3c;
            }
            QPushButton:pressed {
                background-color: #1c1c1c;
            }
        """
        
        equals_button_style = """
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                font-weight: bold;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #106ebe;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """
        
        # 키패드 버튼 생성 (이미지 레이아웃에 맞춤)
        # Row 1: 7, 8, 9, ×
        self._create_button("7", number_button_style, keypad_layout, 0, 0)
        self._create_button("8", number_button_style, keypad_layout, 0, 1)
        self._create_button("9", number_button_style, keypad_layout, 0, 2)
        self._create_button("×", operator_button_style, keypad_layout, 0, 3)
        
        # Row 2: 4, 5, 6, −
        self._create_button("4", number_button_style, keypad_layout, 1, 0)
        self._create_button("5", number_button_style, keypad_layout, 1, 1)
        self._create_button("6", number_button_style, keypad_layout, 1, 2)
        self._create_button("−", operator_button_style, keypad_layout, 1, 3)
        
        # Row 3: 1, 2, 3, +
        self._create_button("1", number_button_style, keypad_layout, 2, 0)
        self._create_button("2", number_button_style, keypad_layout, 2, 1)
        self._create_button("3", number_button_style, keypad_layout, 2, 2)
        self._create_button("+", operator_button_style, keypad_layout, 2, 3)
        
        # Row 4: +/-, 0, ., =
        self._create_button("+/-", operator_button_style, keypad_layout, 3, 0)
        self._create_button("0", number_button_style, keypad_layout, 3, 1)
        self._create_button(".", operator_button_style, keypad_layout, 3, 2)
        self._create_button("=", equals_button_style, keypad_layout, 3, 3)
        
        main_layout.addLayout(keypad_layout)
    
    def _create_button(self, text: str, style: str, layout: QGridLayout, row: int, col: int):
        """
        버튼 생성 및 레이아웃에 추가
        
        Args:
            text: 버튼 텍스트
            style: 버튼 스타일
            layout: 그리드 레이아웃
            row: 행 위치
            col: 열 위치
        """
        button = QPushButton(text)
        button.setStyleSheet(style)
        
        # 버튼 클릭 이벤트 연결
        # functools.partial을 사용하여 클로저 문제 완전 해결
        if text.isdigit() or text == ".":
            # 숫자 버튼: 각 버튼에 고유한 텍스트를 전달
            button.clicked.connect(partial(self._on_number_clicked, text))
        elif text in ["+", "−", "×", "÷"]:
            # 연산자 버튼: 각 버튼에 고유한 연산자를 전달
            button.clicked.connect(partial(self._on_operator_clicked, text))
        elif text == "=":
            # 등호 버튼
            button.clicked.connect(self._on_equals_clicked)
        elif text == "+/-":
            # 부호 변경 버튼
            button.clicked.connect(self._on_sign_change_clicked)
        
        # 레이아웃에 버튼 추가 (이벤트 연결 후)
        layout.addWidget(button, row, col)
    
    def _connect_signals(self):
        """시그널 연결"""
        self.calculation_requested.connect(self._perform_calculation)
    
    def _on_number_clicked(self, digit: str):
        """숫자 버튼 클릭 처리"""
        # 새 피연산자 입력 시작 (연산자 입력 후 또는 초기 상태)
        if self._waiting_for_operand:
            self._current_input = digit
            self._waiting_for_operand = False
        else:
            # 기존 숫자에 추가 입력
            if not self._current_input or self._current_input == "0":
                # 빈 문자열이거나 "0"이면 새 숫자로 교체
                self._current_input = digit
            else:
                # 기존 숫자 뒤에 추가
                self._current_input += digit
        
        self._update_display()
    
    def _on_operator_clicked(self, operator: str):
        """연산자 버튼 클릭 처리"""
        # 연산자 매핑 (GUI 표시 → 내부 연산자)
        operator_map = {
            "+": "+",
            "−": "-",
            "×": "*",
            "÷": "/"
        }
        internal_operator = operator_map.get(operator, operator)
        
        if self._first_number is None:
            # 첫 번째 숫자 입력 완료
            try:
                self._first_number = int(self._current_input)
                self._operator = internal_operator
                self._waiting_for_operand = True
                self._update_input_display()
            except ValueError:
                self.display_error("올바른 숫자를 입력하세요.")
        else:
            # 연산자 변경 또는 계산 후 새 연산자 입력
            if not self._waiting_for_operand:
                # 현재 입력을 두 번째 숫자로 사용하여 계산
                self._on_equals_clicked()
            
            self._operator = internal_operator
            self._waiting_for_operand = True
    
    def _on_equals_clicked(self):
        """등호 버튼 클릭 처리"""
        if self._first_number is not None and self._operator is not None:
            try:
                self._second_number = int(self._current_input)
                self._perform_calculation(self._first_number, self._operator, self._second_number)
            except ValueError:
                self.display_error("올바른 숫자를 입력하세요.")
    
    def _on_sign_change_clicked(self):
        """부호 변경 버튼 클릭 처리"""
        if self._current_input and self._current_input != "0":
            if self._current_input.startswith("-"):
                self._current_input = self._current_input[1:]
            else:
                self._current_input = "-" + self._current_input
            self._update_display()
    
    def _perform_calculation(self, a: int, operator: str, b: int):
        """계산 수행"""
        try:
            result = self._service.calculate(a, operator, b)
            operation_str = self._service.format_operation(a, operator, b, use_gui_display=True)
            
            # 결과 표시
            self.display_result(str(result))
            
            # 계산 과정 표시
            self._input_label.setText(f"{operation_str} =")
            
            # 상태 초기화 (계산 결과를 첫 번째 숫자로 설정)
            self._first_number = result
            self._current_input = str(result)
            self._operator = None
            self._second_number = None
            self._waiting_for_operand = True
            
        except ArithmeticError as e:
            self.display_error(str(e))
            self._reset_calculator()
        except Exception as e:
            self.display_error(f"오류 발생: {e}")
            self._reset_calculator()
    
    def _reset_calculator(self):
        """계산기 상태 초기화"""
        self._first_number = None
        self._operator = None
        self._second_number = None
        self._current_input = ""
        self._waiting_for_operand = True
        self._update_display()
    
    def _update_display(self):
        """디스플레이 업데이트"""
        # 현재 입력값을 결과 라벨에 표시
        display_text = self._current_input if self._current_input else "0"
        self._result_label.setText(display_text)
    
    def _update_input_display(self):
        """입력 디스플레이 업데이트"""
        if self._first_number is not None and self._operator is not None:
            operator_display = {
                "+": "+",
                "-": "−",
                "*": "×",
                "/": "÷"
            }
            op_str = operator_display.get(self._operator, self._operator)
            self._input_label.setText(f"{self._first_number} {op_str}")
    
    # CalculatorView 인터페이스 구현
    def display_input(self, text: str) -> None:
        """입력 내용 표시"""
        self._input_label.setText(text)
    
    def display_result(self, text: str) -> None:
        """결과 표시"""
        self._result_label.setText(text)
    
    def display_error(self, message: str) -> None:
        """오류 메시지 표시"""
        self._result_label.setText(f"오류: {message}")
        self._result_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #ff0000;
                padding: 10px;
                font-size: 18px;
                font-weight: bold;
                color: #ff0000;
            }
        """)
        # 2초 후 스타일 복원
        from PyQt6.QtCore import QTimer
        QTimer.singleShot(2000, lambda: self._result_label.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 1px solid #ccc;
                padding: 10px;
                font-size: 18px;
                font-weight: bold;
            }
        """))
    
    def get_input(self) -> Tuple[int, str, int]:
        """
        사용자로부터 입력을 받음 (GUI에서는 사용하지 않음)
        대신 버튼 클릭으로 입력을 받음
        """
        # GUI에서는 직접 사용하지 않지만 인터페이스 구현을 위해 필요
        return 0, "+", 0
    
    def show_calculation_process(self, operation_str: str) -> None:
        """계산 과정 표시"""
        self._input_label.setText(f"{operation_str}을 계산합니다.")


def main():
    """GUI 애플리케이션 실행"""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

