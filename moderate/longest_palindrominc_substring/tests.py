import program
import unittest


class TestProgram(unittest.TestCase):

    def test_1(self):
        input = "bacc"
        self.assertEqual(program.get_longest_palindromic_substring(input), "cc")

    def test_2(self):
        input = "asdffdsatu"
        self.assertEqual(program.get_longest_palindromic_substring(input), "asdffdsa")

    def test_3(self):
        input = "asdf;ljasdfaaaaasdffdfo"
        self.assertEqual(program.get_longest_palindromic_substring(input), "aaaaa")


if __name__=='__main__':
    unittest.main()
