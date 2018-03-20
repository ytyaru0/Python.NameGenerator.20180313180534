import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'src'))
import unittest
from NameGenerator import NameGenerator
import collections
class NameGeneratorTest(unittest.TestCase):
    def test_0(self):
        args = collections.namedtuple('Namespace', 'extension radix alignment')
        args.extension = 'py'
        args.radix = 10
        args.alignment = False
        args.path_dir_target = str(pathlib.Path(__file__).resolve().parent / 'testdata')
        name = NameGenerator(args).Generate()
        self.assertEqual('0', name)

if __name__ == '__main__':
    unittest.main()
