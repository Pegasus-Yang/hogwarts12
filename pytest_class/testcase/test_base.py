"""
@Author:Pegasus-Yang
@Time: 2020/5/12 下午8:15
"""
import pytest
import sys

sys.path.append('..')
from pytest_class.calculator import Calculator


class TestMath:
    @classmethod
    def setup_class(cls):
        cls.x = {}
        cls.ca = Calculator()

    @pytest.mark.add
    def test_add(self, do_sth):
        result = self.ca.add(1, 2)
        print(do_sth)
        self.x['a'] = result
        assert result == 3

    @pytest.mark.sub
    def test_sub(self, do_sth):
        result = self.ca.sub(2, 1)
        self.x['b'] = result
        print(do_sth)
        print(self.x)
        assert result == 1

@pytest.mark.parametrize('a,b',[[1,2]])
def test_aa(do_sth, a, b):
    print(do_sth)
    print(a)
    print(b)
    print(do_sth)



