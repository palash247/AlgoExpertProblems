import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(program.hasSingleCycle([2, 2, -1]), True)

    def test_case_2(self):
        self.assertEqual(program.hasSingleCycle([2, 2, 2]), True)

    def test_case_3(self):
        self.assertEqual(program.hasSingleCycle([1, 1, 1, 1, 1]), True)

    def test_case_4(self):
        self.assertEqual(program.hasSingleCycle([-1, 2, 2]), True)

    def test_case_5(self):
        self.assertEqual(program.hasSingleCycle([0, 1, 1, 1, 1]), False)

    def test_case_6(self):
        self.assertEqual(program.hasSingleCycle([1, 1, 0, 1, 1]), False)

    def test_case_7(self):
        self.assertEqual(program.hasSingleCycle([1, 1, 1, 1, 2]), False)

    def test_case_8(self):
        self.assertEqual(
            program.hasSingleCycle(
                [3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]
            ),
            True,
        )

    def test_case_9(self):
        self.assertEqual(
            program.hasSingleCycle(
                [3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]
            ),
            False,
        )

    def test_case_10(self):
        self.assertEqual(program.hasSingleCycle([1, 2, 3, 4, -2, 3, 7, 8, 1]), True)

    def test_case_11(self):
        self.assertEqual(program.hasSingleCycle([1, 2, 3, 4, -2, 3, 7, 8, -8]), True)

    def test_case_12(self):
        self.assertEqual(program.hasSingleCycle([1, 2, 3, 4, -2, 3, 7, 8, -26]), True)

    def test_case_13(self):
        self.assertEqual(
            program.hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 908, -26]), True
        )

    def test_case_14(self):
        self.assertEqual(
            program.hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 909, -26]), False
        )

    def test_case_15(self):
        self.assertEqual(program.hasSingleCycle([2, 3, 1, -4, -4, 2]), True)

    def test_case_16(self):
        self.assertEqual(program.hasSingleCycle([1, -1, 1, -1]), False)


if __name__ == "__main__":
    unittest.main()

