import unittest
import funkcje

# stworzymy klasy testowej dziedziczonej po klasie TestCase z modulu  unittest
class TestTDD1(unittest.TestCase):
    # zakladam ze w moim progam ma funkcje zwroc_100
    def test_upper(self):
        # wywylanie metody
                # sle dla klasy z unittest jak i naszej. Porownanie wynik z liczba 100
        self.assertEqual(funkcje.doupper('ddgf'), 'DDGF')

    def test_upper(self):
        pass

    def test_replace(self):
        str = funkcje.do_replace('co'), 'na co')
        self.assertTrue(str.index ('na co')>0)

    def test_title(self):
        self.assertEqual(funkcje.title('jan kowalski'),'Jan Kowalski')

    def test_strip(self):
        self.assertEqual(funkcje.title('  ala  '),'ala')



if __name__ == '__main__':
    unittest.main()
