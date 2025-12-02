import unittest

import year2025_day02a as part_a
import year2025_day02b as part_b


class Test02(unittest.TestCase):

    def test_part_a_with_example_data(self):
        with open('./2025/MZU/02/test-data-a') as file:
            lines = [line.strip() for line in file.readlines()]
            result = part_a.solve(lines)
            self.assertEqual(1227775554, result)
            print(result)

    def test_part_b_with_example_data(self):
        with open('./2025/MZU/02/test-data-b') as file:
            lines = [line.strip() for line in file.readlines()]
            result = part_b.solve(lines)
            self.assertEqual(4174379265, result)
            print(result)


if __name__ == '__main__':
    unittest.main()
