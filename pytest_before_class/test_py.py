"""
@Author:Pegasus-Yang
@Time: 2020/5/7 上午9:16
"""
import allure
import pytest


def setup_function():
    print('setup_function')


def test_case01(before_a):
    print('This is test_case01')


def test_case02():
    print('This is test_case02')
    pytest.assume(1 == 2)
    print('assume pass')
    pytest.assume(1 == 1)


def test_case03(before_a):
    print('This is test_case03')
    raise Exception("This is an Exception")

@allure.feature('中文')
class TestClassDemo():
    @allure.story('010101010101')
    def test_class_case01(self):
        print('This is test_class_case01')

    def test_class_case02(self, before_a):
        print('This is test_class_case02')

    def test_class_case03(self):
        print('This is test_class_case03')


class TestClassDemoOther:
    def test_class_case_a(self):
        print('This is test_class_case_a')

    def test_class_case_b(self):
        print('This is test_class_case_b')

    def test_class_case_c(self):
        print('This is test_class_case_c')

