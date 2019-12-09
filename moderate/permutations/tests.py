import program
import unittest

class TestPermutations(unittest.TestCase):

    def test_len(self):
        self.assertTrue(len(program.get_permutations([1,2,3]))==6)

    def test_permutations(self):
        self.assertEqual(program.get_permutations([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])

if __name__=='__main__':
    unittest.main()
