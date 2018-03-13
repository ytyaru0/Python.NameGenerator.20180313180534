import glob
import os.path

class NameGenerator:
    def __init__(self, path):
        self.__path = path
        self.__files = []
        if not os.path.isdir(path): raise Exception('存在するディレクトリのパスを指定して下さい。: {}'.format(path))

    def Generate(self, ext=None):
        self.__GetFileNames(ext)
        print(self.__files)
        return self.__FindMin(0)

    def __GetFileNames(self, ext):
        reg = '*'
        if ext is not None:
            if ext.startswith('.'): reg += ext
            else: reg += '.{}'.format(ext)
        self.__files.clear()
        for path in glob.glob(os.path.join(self.__path, reg)):
            self.__files.append(os.path.splitext(os.path.basename(path))[0])
        sorted(self.__files)

    def __FindMin(self, count:int):
        print('count:', count)
        for f in self.__files:
            if f == self.__GetCountName(count): return self.__FindMin((count+1))
        return self.__GetCountName(count)

    def __GetCountName(self, count:int):
        if -1 < count and count < 10: return str(count)
        elif 9 < count and count < 37: return chr(97 + (count - 10))
        else: raise Exception('未実装。count={}以上の値でファイル名を作れません。'.format(count))


if __name__ == '__main__':
    """
    import sys
    if len(sys.argv) < 2: raise Exception('起動引数が足りません。存在するディレクトリのパスを渡して下さい。')
    path = sys.argv[1]
    ext = None
    if 2 < len(sys.argv): ext = sys.argv[2]
    print(NameGenerator(path).Generate(ext))
    """
    import argparse
    parser = argparse.ArgumentParser(
        description='NameGenerator.',
    )
    parser.add_argument('path_dir_target')
    parser.add_argument('-e', '--extension')    # 拡張子
    parser.add_argument('-r', '--radix')        # 基数
    parser.add_argument('-a', '--alignment', action='store_true') # 桁合わせ
    args = parser.parse_args()
    if args.path_dir_target is None: raise Exception('起動引数が足りません。存在するディレクトリのパスを渡して下さい。')
    print(NameGenerator(args.path_dir_target).Generate(args.extension))

