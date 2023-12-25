import unittest

import year2023_day24a as part_a
import year2023_day24b as part_b


class Test(unittest.TestCase):

    def test_part_a_with_example_data(self):
        with open('test-data-a') as file:
            lines = [line.strip() for line in file.readlines()]
            result = part_a.solve(lines, 7, 27)
            self.assertEqual(2, result)
            print(result)

    def test_part_b_with_example_data(self):
        with open('test-data-b') as file:
            lines = [line.strip() for line in file.readlines()]
            result = part_b.solve(lines)
            self.assertEqual(47, result)
            print(result)


if __name__ == '__main__':
    unittest.main()
