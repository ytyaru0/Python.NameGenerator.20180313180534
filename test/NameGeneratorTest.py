import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'src'))
import unittest
from NameGenerator import NameGenerator
import collections
import shutil
class NameGeneratorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__path_dir_test_data = (pathlib.Path(__file__).resolve().parent / 'testdata')
    def __del__(self, *args, **kwargs):
        if self.__path_dir_test_data.is_dir():
            shutil.rmtree(self.__path_dir_test_data)
    def __create_test_args(self, ext=None, radix=10, align=False):
        args = collections.namedtuple('Namespace', 'extension radix alignment')
        args.extension = ext
        args.radix = radix
        args.alignment = align
        args.path_dir_target = str(self.__path_dir_test_data)
        return args
    def __create_test_data(self, args, num=0):
        path = pathlib.Path(args.path_dir_target)
        if path.is_dir(): shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)
        if 0 == num: return
        for i in range(0, num):
            name = NameGenerator(args).Generate()
            if args.extension is not None:
                filename = name + '.' + args.extension
                with open(path / filename, 'w'): pass
            else:
                (pathlib.Path(path)/name).mkdir(parents=True, exist_ok=True)

    def test_0(self):
        args = self.__create_test_args(ext='py', radix=10, align=False)
        self.__create_test_data(args)
        name = NameGenerator(args).Generate()
        self.assertEqual('0', name)

    def test_1(self):
        args = self.__create_test_args(ext='py', radix=10, align=False)
        self.__create_test_data(args, 1)
        name = NameGenerator(args).Generate()
        self.assertEqual('1', name)

    def test_9(self):
        args = self.__create_test_args(ext='py', radix=10, align=False)
        self.__create_test_data(args, 10)
        name = NameGenerator(args).Generate()
        self.assertEqual('10', name)
        for i in range(0, 10):
            self.assertTrue((pathlib.Path(args.path_dir_target).resolve() / (str(i) + '.py')).is_file())

    def test_10(self):
        args = self.__create_test_args(ext='py', radix=10, align=False)
        self.__create_test_data(args, 11)
        name = NameGenerator(args).Generate()
        self.assertEqual('11', name)
        for i in range(0, 11):
            self.assertTrue((pathlib.Path(args.path_dir_target).resolve() / (str(i) + '.py')).is_file())

    def test_9_align(self):
        args = self.__create_test_args(ext='py', radix=10, align=True)
        self.__create_test_data(args, 10)
        name = NameGenerator(args).Generate()
        self.assertEqual('10', name)
        for i in range(0, 10):
            self.assertTrue((pathlib.Path(args.path_dir_target).resolve() / ('0' + str(i) + '.py')).is_file())

    def test_0_dir(self):
        args = self.__create_test_args(ext=None, radix=10, align=True)
        self.__create_test_data(args)
        name = NameGenerator(args).Generate()
        self.assertEqual('0', name)

    def test_1_dir(self):
        args = self.__create_test_args(ext=None, radix=10, align=True)
        self.__create_test_data(args, 1)
        name = NameGenerator(args).Generate()
        self.assertEqual('1', name)


    def test_all_0(self):
        exts = [None, 'py', 'sh', 'md']
        radixs = [10, 2, 8, 16, 36]
        aligns = [False, True]
        for ext in exts:
            for radix in radixs:
                for align in aligns:
                    args = self.__create_test_args(ext=ext, radix=radix, align=align)
                    self.__create_test_data(args)
                    name = NameGenerator(args).Generate()
                    self.assertEqual('0', name)

    def test_all_1(self):
        exts = [None, 'py', 'sh', 'md']
        radixs = [10, 2, 8, 16, 36]
        aligns = [False, True]
        for ext in exts:
            for radix in radixs:
                for align in aligns:
                    with self.subTest(ext=ext, radix=radix, align=align):
                        args = self.__create_test_args(ext=ext, radix=radix, align=align)
                        self.__create_test_data(args, 1)
                        name = NameGenerator(args).Generate()
                        self.assertEqual('1', name)
           
    def test_all_9(self):
        exts = [None, 'py']
        radixs = [10, 2, 8, 16, 26, 32, 36, 64]
        aligns = [False, True]
        for ext in exts:
            for radix in radixs:
                for align in aligns:
                    with self.subTest(ext=ext, radix=radix, align=align):
                        args = self.__create_test_args(ext=ext, radix=radix, align=align)
                        self.__create_test_data(args, radix)
                        name = NameGenerator(args).Generate()
                        self.assertEqual(NameGenerator(args).Characters[radix][1]+NameGenerator(args).Characters[radix][0], name)
                        for i in range(0, radix):
                            if align:
                                name = NameGenerator(args).Characters[radix][0]+NameGenerator(args).Characters[radix][i]
                            else:
                                name = NameGenerator(args).Characters[radix][i]
                            if args.extension is not None:
                                filename = name + '.' + ext
                                self.assertTrue((pathlib.Path(args.path_dir_target)/filename).is_file())
                            else:
                                self.assertTrue((pathlib.Path(args.path_dir_target)/name).is_dir())


if __name__ == '__main__':
    unittest.main()
