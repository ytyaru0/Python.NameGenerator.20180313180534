import glob
import os.path
import string
import math

# ファイル数から名前を生成する
class NameGenerator:
    def __init__(self, args):
        self.__args = args
        self.__files = []
        if not os.path.isdir(self.__args.path_dir_target): raise Exception('存在するディレクトリのパスを指定して下さい。: {}'.format(self.__args.path_dir_target))
        self.__bases = { 2: string.digits[:2], 
                         8: string.digits[:8], 
                        10: string.digits, 
                        16: string.digits + string.ascii_lowercase[:6],
                        26:                 string.ascii_lowercase,
                        32: string.digits + string.ascii_lowercase[:22],
                        36: string.digits + string.ascii_lowercase,
                        64: string.digits + string.ascii_lowercase + string.ascii_uppercase + '_-',
                        # Win, Mac, Linuxでパスに使える記号を追加。使えない印字可能文字は\/:*?"<>|
                        85: string.digits + string.ascii_lowercase + string.ascii_uppercase + "!#$%&'()-=~^@`[]{};+,._"}

    def Generate(self):
        self.__GetFileNames()
        print(self.__files)
        count = len(self.__files)
        name = self.__GetCountName(count)
        self.__Alignment(count)
        return name

    def __GetFileNames(self):
        reg = '*'
        if self.__args.extension is not None:
            if self.__args.extension.startswith('.'): reg += self.__args.extension
            else: reg += '.{}'.format(self.__args.extension)
        self.__files.clear()
        for path in glob.glob(os.path.join(self.__args.path_dir_target, reg)):
            if self.__args.extension is None:
                if os.path.isdir(path): self.__files.append(os.path.basename(path))
            else:
                if os.path.isfile(path): self.__files.append(os.path.splitext(os.path.basename(path))[0])
        sorted(self.__files)

    def __GetCountName(self, count:int):
        chars = self.__bases[self.__args.radix]
        if count < len(chars): return (chars)[count]
        else: return self.__GetCountName(count // len(chars)) + (chars)[count % len(chars)]

    # 10.pyの名前が出力された直後、0.pyを00.pyとしたい
    def __Alignment(self, count):
        if self.__args.alignment and (count == len(self.__files)):
            import os
            prefix = self.__bases[self.__args.radix][0]
            for name in self.__files:
                fig = math.floor(math.log(count, self.__args.radix)) + 1
                if self.__args.extension: ext = '.' + self.__args.extension
                else: ext = ''
                os.rename(
                    os.path.join(self.__args.path_dir_target, name+ext), 
                    os.path.join(self.__args.path_dir_target, prefix*(fig - len(name)) + name+ext))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='NameGenerator.',
    )
    parser.add_argument('path_dir_target')
    parser.add_argument('-e', '--extension')                                        # 拡張子
    parser.add_argument('-r', '--radix', type=int, default=10)                      # 基数
    parser.add_argument('-a', '--alignment', action='store_true', default=False)    # 桁合わせ
    args = parser.parse_args()
    if args.path_dir_target is None: raise Exception('起動引数が足りません。存在するディレクトリのパスを渡して下さい。')
    print(NameGenerator(args).Generate())

