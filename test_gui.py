"""
GUI 계산기 테스트 스크립트
실제로 작동하는지 확인
"""
import sys
from PyQt6.QtWidgets import QApplication
from gui_calculator_view import CalculatorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    print("계산기 GUI가 실행되었습니다.")
    print("숫자 버튼을 클릭하여 테스트하세요.")
    sys.exit(app.exec())

