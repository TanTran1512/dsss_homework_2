import unittest
from math_quiz import generate_integer, generate_operator, calculation


class TestMathGame(unittest.TestCase):

    def generate_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def generate_operator(self):
        # Test if generated operators are of the four expected symbols
        operator = generate_operator()
        self.assertIn(operator, ['+', '-', '*'])


    def calculation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7), (3, 2, '-', '3-2', 1), (4, 3, '*', '4 * 3', '12')
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculation(num1, num2, operator)
                # Check if function returns match the expected values
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
