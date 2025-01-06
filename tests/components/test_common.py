import unittest

from holos_service.components import common


class TestComponentType(unittest.TestCase):
    def test_to_str(self):
        for component_type in common.ComponentType:
            self.assertEqual(
                component_type.value,
                component_type.to_str().replace('Component', '')
            )


if __name__ == '__main__':
    unittest.main()
