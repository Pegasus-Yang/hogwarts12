"""
@Author:Pegasus-Yang
@Time: 2020/5/6 下午10:52
"""

import unittest


class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_case01(self):
        print('test_case01')
        self.assertEqual('a', 'a', '判断case01')

    def test_case02(self):
        print('test_case02')
        self.assertEqual('b', 'b', '判断case02')

    # @unittest.skip
    def test_case03(self):
        print('test_case03')
        self.assertEqual('c', 'c', '判断case03')


class TestDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_case01(self):
        print('test_case01')
        self.assertEqual('a', 'a', '判断case01')

    def test_case02(self):
        print('test_case02')
        self.assertEqual('b', 'b', '判断case02')

    # @unittest.skip
    def test_case03(self):
        print('test_case03')
        self.assertEqual('c', 'c', '判断case03')


if __name__ == '__main__':
    unittest.main()
