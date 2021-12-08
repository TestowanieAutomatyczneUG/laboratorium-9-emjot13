from lab9.zad3.src.checker import Checker
from lab9.zad3.src.environment import Class

import unittest
from unittest.mock import *

class Tests(unittest.TestCase):
    def test_after_17(self):
        obj = Class()
        obj.getTime = Mock()
        obj.getTime.return_value = 18
        test = Checker(obj)
        test.remainder("file")
        self.assertEqual(test.fileWasPlayed, True)


    def test_before_17(self):
        obj = Class()
        obj.getTime = Mock()
        obj.getTime.return_value = 18
        test = Checker(obj)
        test.remainder("file")
        self.assertEqual(test.fileWasPlayed, False)

