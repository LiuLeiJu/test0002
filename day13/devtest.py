from unittest import TestCase
from demo import Calc

class testCalc(TestCase):

    def testDev1(self):

         a = 6
         b = 3
         c = 2

         calc = Calc()
         sum = calc.devision(a,b)

         self.assertEqual(c,sum)

    def testDev2(self):
        a = 6
        b = 3
        c = -2

        calc = Calc()
        sum = calc.devision(a, b)

        self.assertEqual(c, sum)