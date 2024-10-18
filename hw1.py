import unittest
from unittest import TestCase
from forTest import Runner


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('John')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Hamish')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('William')
        runner2 = Runner('Sherlock')
        for _ in range(10):
            runner1.walk()
        for _ in range(10):
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)
