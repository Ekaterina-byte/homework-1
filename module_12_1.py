'''
класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

'''
import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        func_runner = Runner('Walk')
        for i in range(10):
            func_runner.walk()
        self.assertEqual(func_runner.distance, 50)

    def test_run(self):
        func_runner = Runner('Run')
        for i in range(10):
            func_runner.run()
        self.assertEqual(func_runner.distance, 100)

    def test_chellenger(self):
        func_runner = Runner('Walk_1')
        func_runner_1 = Runner('Run_1')
        for i in range(10):
            func_runner.walk()
            func_runner_1.run()
        self.assertNotEqual(func_runner.distance, func_runner_1.distance)

if __name__ =='__main__':
    unittest.main()
        

