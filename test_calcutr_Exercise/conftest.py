import pytest
import yaml


def get_data():
    data = yaml.safe_load(open("./data.yml"))
    return data


@pytest.fixture(scope="module")
def my_fixture():
    print("开始计算")
    yield
    print("计算结束")
