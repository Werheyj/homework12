import unittest
from unittest import TestCase
from forTest3 import Runner
import logging


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner('John', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(40)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Hеверный тип данных для объекта Runner')

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('William')
        runner2 = Runner('Sherlock')
        for _ in range(10):
            runner1.walk()
        for _ in range(10):
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)
