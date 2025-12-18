"""
GUI 계산기 간단 테스트 스크립트
숫자 버튼 클릭이 제대로 작동하는지 확인
"""
import sys
from PyQt6.QtWidgets import QApplication
from gui_calculator_view import CalculatorWindow

def test_number_buttons():
    """숫자 버튼 테스트"""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    
    # 초기 상태 확인
    print(f"초기 상태:")
    print(f"  _current_input: {window._current_input}")
    print(f"  _waiting_for_operand: {window._waiting_for_operand}")
    print(f"  결과 라벨 텍스트: {window._result_label.text()}")
    
    # 숫자 버튼 클릭 시뮬레이션
    print("\n숫자 '1' 버튼 클릭 시뮬레이션:")
    window._on_number_clicked("1")
    print(f"  _current_input: {window._current_input}")
    print(f"  _waiting_for_operand: {window._waiting_for_operand}")
    print(f"  결과 라벨 텍스트: {window._result_label.text()}")
    
    print("\n숫자 '2' 버튼 클릭 시뮬레이션:")
    window._on_number_clicked("2")
    print(f"  _current_input: {window._current_input}")
    print(f"  결과 라벨 텍스트: {window._result_label.text()}")
    
    print("\n✅ 테스트 완료. GUI 창이 열리면 숫자 버튼을 클릭해보세요.")
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    test_number_buttons()

