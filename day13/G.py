

from  HTMLTestRunner import HTMLTestRunner
import unittest

#1.将所有用例全部加载出来
tests = unittest.defaultTestLoader.discover(r"E:\PythonTest",pattern="*test.py")


#2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算机测试报告",
    description = "这是计算机的假发测试报告",
    verbosity=1,
    stream= open(file="计算机报告.html",mode="w+",encoding="utf-8")
)



#3.让运行器运行用例，并生成测试报告
runner.run(tests)







