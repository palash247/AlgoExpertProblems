import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.selectionSort([1,-99,99,0,100]), [-99, 0, 1, 99, 100])

if __name__ == "__main__":
    unittest.main()

