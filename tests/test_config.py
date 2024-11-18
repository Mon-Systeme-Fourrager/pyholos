import unittest

from holos_service import config


class TestPaths(unittest.TestCase):
    def test_paths_exist(self):
        for pth in [config.PATH_HOLOS_CLI,
                    config.PATH_SLC_GEOJSON_FILE]:
            self.assertTrue(pth.exists(), msg=self._set_error_message(pth))

    @staticmethod
    def _set_error_message(s: str):
        return f'The following file is missing:\n{s}'


if __name__ == '__main__':
    unittest.main()
