# import unittest
# from my_calculator import my_adder
#
# class TestMyAdder(unittest.TestCase):        # Test开头表示这是一个用于测试的类，它是unittest.TestCase的子类
#     def test_positive_with_positive(self):   # 测试用例是库下面的一个方法 这是正数加正数
#         assert my_adder(3,2) == 5
#
#     def test_negative_with_positive(self):   # 正数加负数
#         assert my_adder(-3,2) == -1


import unittest
from my_calculator import my_adder

class TestMyAdder(unittest.TestCase):        # Test开头表示这是一个用于测试的类，它是unittest.TestCase的子类
    def test_positive_with_positive(self):   # 测试用例是库下面的一个方法 这是正数加正数
        self.assertEqual(my_adder(3,2) , 5)

    def test_negative_with_positive(self):   # 正数加负数
        self.assertEqual(my_adder(-3,2) , -1)
