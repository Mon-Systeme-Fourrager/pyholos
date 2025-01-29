import unittest

from holos_service import utils


class TestConvertCamelCaseToSpaceDelimited(unittest.TestCase):
    def test_expected_values(self):
        for input_str, expected_str in [
            ("CamelCase", "Camel Case"),
            ("camelCase", "camel Case"),
            ("Notcamelcase", "Notcamelcase"),
            ("snake_case", "snake_case"),
        ]:
            self.assertEqual(
                expected_str,
                utils.convert_camel_case_to_space_delimited(s=input_str)
            )


class TestCalcAverage(unittest.TestCase):
    def test_values(self):
        for values, expected_result in [
            ([1, 2, 3], 2),
            (range(10), 4.5),
            ((v for v in range(10)), 4.5),
            ((3, 3, 3), 3),
            ((-1, 1), 0)
        ]:
            self.assertEqual(
                expected_result,
                utils.calc_average(values=values))


if __name__ == '__main__':
    unittest.main()
