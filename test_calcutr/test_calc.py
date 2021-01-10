import pytest

from test_calcutr.test_calculator import TestCalculator


class TestCalc:
    def setup_class(self):
        self.calc = TestCalculator()
        print("开始计算")

    @pytest.mark.parametrize("a, b, expect", [
        (1, 2, 3), (-1, -2, -3), (3.2, 3.3, 6.5), ("a", "b", "ab")
    ], ids=["int", "minus", "Decimal", "str"])
    def test_add(self, a, b, expect):
        assert expect == self.calc.test_add(a, b)
        print(f"{a}+{b}={expect}")

    @pytest.mark.parametrize("a, b, expect", [
        (6, 2, 4), (-3, -2, -1), (6.5, 3.3, 3.2)
    ], ids=["int", "minus", "Decimal"])
    def test_subtract(self, a, b, expect):
        assert expect == self.calc.test_subtract(a, b)
        print(f"{a}-{b}={expect}")

    @pytest.mark.parametrize("a, b, expect", [
        (6, 2, 12), (-3, -2, 6), (6.5, 3.3, 21.45)
    ], ids=["int", "minus", "Decimal"])
    def test_multiply(self, a, b, expect):
        assert expect == self.calc.test_multiply(a, b)
        print(f"{a}*{b}={expect}")

    @pytest.mark.parametrize("a, b, expect", [
        (6, 2, 3), (-3, -2, 1.5), (6.5, 3.25, 2)
    ], ids=["int", "minus", "Decimal"])
    def test_divide(self, a, b, expect):
        assert expect == self.calc.test_divide(a, b)
        print(f"{a}/{b}={expect}")

    def teardown_class(self):
        print("结束计算")
