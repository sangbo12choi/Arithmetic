"""
사칙연산 모듈 테스트 파일
TC-CMM-001 / TC-AO-001
TDD RED 단계: 실패하는 테스트 작성
"""

import unittest
from arithmetic import Arithmetic


class TestArithmetic(unittest.TestCase):
    """사칙연산 모듈 테스트 클래스"""

    def setUp(self):
        """테스트 전 초기화"""
        self.calc = Arithmetic()

    def test_add_positive_numbers(self):
        """양수 덧셈 테스트: 1 + 10 = 11"""
        result = self.calc.add(1, 10)
        self.assertEqual(result, 11, "1 + 10은 11이어야 합니다")

    def test_add_zero_and_positive(self):
        """0과 양수 덧셈 테스트: 0 + 1 = 1"""
        result = self.calc.add(0, 1)
        self.assertEqual(result, 1, "0 + 1은 1이어야 합니다")

    def test_add_negative_numbers(self):
        """음수 덧셈 테스트: -1 + (-10) = -11"""
        result = self.calc.add(-1, -10)
        self.assertEqual(result, -11, "-1 + (-10)은 -11이어야 합니다")

    def test_subtract_positive_numbers(self):
        """양수 뺄셈 테스트: 5 - 2 = 3"""
        result = self.calc.subtract(5, 2)
        self.assertEqual(result, 3, "5 - 2는 3이어야 합니다")

    def test_multiply_negative_numbers(self):
        """음수 곱셈 테스트: -5 * -3 = 15"""
        result = self.calc.multiply(-5, -3)
        self.assertEqual(result, 15, "-5 * -3은 15이어야 합니다")

    def test_multiply_by_zero(self):
        """0 곱셈 테스트: 0 * 10 = 0"""
        result = self.calc.multiply(0, 10)
        self.assertEqual(result, 0, "0 * 10은 0이어야 합니다")

    def test_divide_integer(self):
        """정수 나눗셈 테스트: 5 / 2 = 2"""
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2, "5 / 2는 2이어야 합니다 (정수 나눗셈)")

    def test_divide_quotient(self):
        """소수점 나눗셈 테스트: 5 ÷ 2 = 2.5"""
        result = self.calc.quotient(5, 2)
        self.assertEqual(result, 2.5, "5 ÷ 2는 2.5이어야 합니다")

    def test_divide_negative_by_positive(self):
        """음수를 양수로 나누기 테스트: -10 / 2 = -5"""
        result = self.calc.divide(-10, 2)
        self.assertEqual(result, -5, "-10 / 2는 -5이어야 합니다")

    def test_divide_by_zero(self):
        """0으로 나누기 예외 테스트: 0 / 0 = ArithmeticException"""
        with self.assertRaises(ArithmeticError):
            self.calc.divide(0, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)

