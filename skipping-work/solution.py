
import unittest

def solution(x, y):
    x_sum = sum(x)
    y_sum = sum(y)
    return x_sum - y_sum if len(x) > len(y) else y_sum - x_sum



class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]), -4, "Should be -4")

    def test_2(self):
        self.assertEqual(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()