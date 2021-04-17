import unittest
import marks


class TestCalc(unittest.TestCase):

    def test_determineMark(self):
        result= marks.determineMark(67)
        self.assertEqual(result, 4)


    if __name__== '__main__':
        unittest.main()