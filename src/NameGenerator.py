import glob
import os.path

class NameGenerator:
    def __init__(self, args):
        self.__args = args
        self.__files = []
        if not os.path.isdir(self.__args.path_dir_target): raise Exception('存在するディレクトリのパスを指定して下さい。: {}'.format(self.__args.path_dir_target))

    def Generate(self):
        self.__GetFileNames()
        print(self.__files)
        return self.__FindMin(0)

    def __GetFileNames(self):
        reg = '*'
        if self.__args.extension is not None:
            if self.__args.extension.startswith('.'): reg += self.__args.extension
            else: reg += '.{}'.format(self.__args.extension)
        self.__files.clear()
        for path in glob.glob(os.path.join(self.__args.path_dir_target, reg)):
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
    import argparse
    parser = argparse.ArgumentParser(
        description='NameGenerator.',
    )
    parser.add_argument('path_dir_target')
    parser.add_argument('-e', '--extension')                                        # 拡張子
    parser.add_argument('-r', '--radix', default=10)                                # 基数
    parser.add_argument('-a', '--alignment', action='store_true', default=False)    # 桁合わせ
    args = parser.parse_args()
    if args.path_dir_target is None: raise Exception('起動引数が足りません。存在するディレクトリのパスを渡して下さい。')
    print(NameGenerator(args).Generate())

