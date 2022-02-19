import code
import unittest

class Test(unittest.TestCase):

    def test_1(self):
        file1 = open("answers.txt","a+")
        try:
            self.assertEqual(code.add(1,1), 2)
            self.assertEqual(code.add(1,-1), 0)
            file1.write('done \n')
            file1.close()
        except Exception:
            file1.write('not \n')
            file1.close()

if __name__ == '__main__':
    unittest.main()