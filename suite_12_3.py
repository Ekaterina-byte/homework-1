import unittest
import module_12_3 as m12_3

test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(m12_3.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(m12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)
