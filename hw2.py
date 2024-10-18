import unittest
from unittest import TestCase
from forTest2 import Runner, Tournament


class TournamentTest(TestCase):
    is_frozen = True

    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for name, result in cls.all_results.items():
            print(f'{name}: {result}')

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        finishers = tournament.start()
        last_finisher = finishers[max(finishers.keys())]
        last_finisher_name = last_finisher.name
        self.assertTrue(last_finisher_name == 'Ник')

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        finishers = tournament.start()
        last_finisher = finishers[max(finishers.keys())]
        last_finisher_name = last_finisher.name
        self.assertTrue(last_finisher_name == 'Ник')

    @unittest.skipUnless(not is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        finishers = tournament.start()
        last_finisher = finishers[max(finishers.keys())]
        last_finisher_name = last_finisher.name
        self.assertTrue(last_finisher_name == 'Ник')
