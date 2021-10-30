import pytest

from main.MyClass import MyClass


@pytest.mark.parametrize('a,b', [(2, 3), (3, 4), (3, 5), (5, 9)])
def test_add(a, b):
    mc = MyClass()

    assert b == mc.add(1, a)
