import unittest
import hw1
import hw2


run_tour_TS = unittest.TestSuite()

run_tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(hw1.RunnerTest))
run_tour_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(hw2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour_TS)
