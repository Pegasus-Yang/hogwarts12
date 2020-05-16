"""
@Author:Pegasus-Yang
@Time: 2020/5/7 下午3:29
"""
import pytest

# @pytest.mark.parametrize(indirect=True)
@pytest.fixture(scope='module')
def before_a():
    print('提前执行')
    yield
    print('yield扫尾')
