"""
@Author:Pegasus-Yang
@Time: 2020/5/14 下午1:53
"""
import pytest


def pytest_collection_modifyitems(session, config, items):
    for i in items:
        print('collection')
        print(i)


@pytest.fixture(scope='class')
def do_sth():
    print('before')
    yield 1
    print('after')
