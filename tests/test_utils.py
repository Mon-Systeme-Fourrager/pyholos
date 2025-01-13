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


if __name__ == '__main__':
    unittest.main()
