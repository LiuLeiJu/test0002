from unittest import TestCase
from demo import Calc

class testCalc(TestCase):

    def testMul1(self):

         a = 6
         b = 7
         c = 42

         calc = Calc()
         sum = calc.multi(a,b)

         self.assertEqual(c,sum)

    def testMul2(self):
        a = 6
        b = 7
        c = -42

        calc = Calc()
        sum = calc.multi(a, b)

        self.assertEqual(c, sum)