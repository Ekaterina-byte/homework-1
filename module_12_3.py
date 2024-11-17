import unittest
from unittest import TestCase

import Module_12_2 as M

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        m1 = M.Runner("member1")
        for _ in range(10):
            m1.walk()
        self.assertEqual(m1.distance, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        m2 = M.Runner("member2")
        for _ in range(10):
            m2.run()
        self.assertEqual(m2.distance, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        m3 = M.Runner("member3")
        m4 = M.Runner("member4")
        for _ in range(10):
            m3.walk()
            m4.run()
        self.assertNotEqual(m3.distance, m4.distance)

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class TournamentTest(TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_variants = []


    def setUp(self):
        self.first = Runner("Усэйн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_variants):
            print(i, elem)
    @ unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test(self):
        tournament1 = R.Tournament(90, self.first, self.third)
        results1 = tournament1.start()
        TournamentTest.all_variants.append(results1)
        self.assertTrue(results1[2] == 'Ник')

    @ unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test1(self):
        tournament2 = R.Tournament(90, self.second, self.third)
        results2 = tournament2.start()
        TournamentTest.all_variants.append(results2)
        self.assertTrue(results2[2] == 'Ник')

    @ unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test2(self):
        tournament3 = R.Tournament(90, self.first, self.second, self.third)
        results3 = tournament3.start()
        TournamentTest.all_variants.append(results3)
        self.assertTrue(results3[3] == 'Ник')
