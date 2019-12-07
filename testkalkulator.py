import unittest
import kalkulator

# stworzymy klasy testowej dziedziczonej po klasie TestCase z modulu  unittest
class TestTDD1(unittest.TestCase):
    # zakladam ze w moim progam ma funkcje zwroc_100
    def test_dodawanie(self):
        # wywylanie metody
        wynik = kalkulator.dodawanie()
        # sle dla klasy z unittest jak i naszej. Porownanie wynik z liczba 100
        self.assertEqual(wynik, 7)




if __name__ == '__main__':
    unittest.main()
