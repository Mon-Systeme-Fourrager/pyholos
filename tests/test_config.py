import unittest

from holos_service import config


class TestPaths(unittest.TestCase):
    def test_paths_exist(self):
        self.assertTrue(config.PATH_HOLOS_CLI)

        for pth in config.PathsSlcData:
            self.assertTrue(pth.value.exists(), msg=self._set_error_message(pth.value))

    @staticmethod
    def _set_error_message(s: str):
        return f'The following file is missing:\n{s}'


if __name__ == '__main__':
    unittest.main()
