import unittest

from holos_service import config


class TestPaths(unittest.TestCase):
    def test_paths_exist(self):
        self.assertIsNotNone(config.PATH_HOLOS_CLI)

        for pth in config.PathsSlcData:
            print(pth.value, pth.value.exists())
            self.assertTrue(pth.value.exists())

if __name__ == '__main__':
    unittest.main()
