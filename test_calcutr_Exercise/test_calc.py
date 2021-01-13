import allure
import pytest
from test_calcutr_Exercise.conftest import get_data
from test_calcutr_Exercise.calculator import Calculator

# data = yaml.safe_load(open("./data.yml"))
c = Calculator()


@allure.feature("计算模块")
class TestCalc:
    @allure.title("相加计算")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("a, b, expect",
                             get_data()['add'],
                             ids=get_data()['ids'])
    def test_add(self, a, b, expect, my_fixture):
        assert expect == c.add(a, b)
        print(f"{a}+{b}={expect}")

    @allure.title("相减计算")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expect",
                             get_data()['subtract'],
                             ids=get_data()['ids'])
    def test_subtract(self, a, b, expect, my_fixture):
        assert expect == c.subtraction(a, b)
        print(f"{a}-{b}={expect}")

    @allure.title("相乘计算")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a, b, expect",
                             get_data()["multiply"],
                             ids=get_data()["ids"]
                             )
    def test_multiply(self, a, b, expect, my_fixture):
        assert expect == c.multiply(a, b)
        print(f"{a}*{b}={expect}")

    @allure.title("相除计算")
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a, b, expect",
                             get_data()['divide'],
                             ids=get_data()['ids'])
    def test_divide(self, a, b, expect, my_fixture):
        assert expect == c.divide(a, b)
        print(f"{a}/{b}={expect}")
