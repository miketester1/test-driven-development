import unittest
import helloworld

# stworzymy klasy testowej dziedziczonej po klasie TestCase z modulu  unittest
class TestTDD1(unittest.TestCase):
    # zakladam ze w moim progam ma funkcje zwroc_100
    def test_printhello(self):
        # wywylanie metody
        wynik = helloworld.printhello()
        # sle dla klasy z unittest jak i naszej. Porownanie wynik z liczba 100
        self.assertEqual(wynik, "hello world")




if __name__ == '__main__':
    unittest.main()
