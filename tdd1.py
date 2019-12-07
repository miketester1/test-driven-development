

#class TestTDD1(unittest.TestCase): #dziedzicze po klasie TestCase
#    def test_zwroc_100(self):         #tworze metody testowe - funkcjonalnosci z przedrostkiem test
#        wynik = mojprogram.zwroc_100()
#        self.assertEqual(wynik, 100)

#    def test_zwroc_paramametr(self):
        #wynik = mojprogram.zwroc_parametr(124)
#        self.assertEqual(mojprogram.test_zwroc_paramametr(124, 124)


import unittest
import mojprogram

# stworzymy klasy testowej dziedziczonej po klasie TestCase z modulu  unittest
class TestTDD1(unittest.TestCase):
    # zakladam ze w moim progam ma funkcje zwroc_100
    def test_zwroc_100(self):
        # wywylanie metody
        wynik = mojprogram.zwroc_100()
        # sle dla klasy z unittest jak i naszej. Porownanie wynik z liczba 100
        self.assertEqual(wynik, 100)



    def test_zwroc_parametr(self):
        wynik = mojprogram.zwroc_parametr(124)
        self.assertEqual(wynik, 124)


if __name__ == '__main__':
    unittest.main()
