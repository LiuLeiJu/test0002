

from unittest import TestCase
from demo import Calc

class testCalc(TestCase):

    def testAdd1(self):

         a = 6
         b = 7
         c = 13

         calc = Calc()
         sum = calc.add(a,b)

         self.assertEqual(c,sum)


    def testAdd2(self):
          a = 6
          b = 7
          c = -13

          calc = Calc()
          sum = calc.add(a, b)

          self.assertEqual(c, sum)

