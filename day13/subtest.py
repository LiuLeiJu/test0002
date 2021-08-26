from unittest import TestCase
from demo import Calc

class testCalc(TestCase):

    def testSub1(self):

         a = 6
         b = 7
         c = -1

         calc = Calc()
         sum = calc.subs(a,b)

         self.assertEqual(c,sum)

    def testSub2(self):
        a = 6
        b = 7
        c = 1

        calc = Calc()
        sum = calc.subs(a, b)

        self.assertEqual(c, sum)