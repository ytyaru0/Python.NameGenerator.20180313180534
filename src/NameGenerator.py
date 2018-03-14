import glob
import os.path
import string

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
        #if -1 < count and count < 10: return str(count)
        #elif 9 < count and count < 37: return chr(97 + (count - 10))
        #else: raise Exception('未実装。count={}以上の値でファイル名を作れません。'.format(count))
        if 10 == self.__args.radix: return self.__GetCountName10(0)
        elif 16 == self.__args.radix: return self.__GetCountName16(0)
        elif 26 == self.__args.radix: return self.__GetCountName26(0)
        elif 36 == self.__args.radix: return self.__GetCountName36(0)
        else: raise Exception('未実装。基数が {} では値を作れません。'.format(args.radix))

    def __GetCountName10(self, count:int): return str(count)
    def __GetCountName16(self, count:int): return '{:x}'.format(count)
    def __GetCountName26(self, count:int):
        base = string.ascii_lowercase
        if count < len(base): return (base)[count]
        else: return GetCountName26(count // len(base)) + (base)[count % len(base)]
    # https://teratail.com/questions/95208
    def __GetCountName36(self, count:int):
        base = string.digits + string.ascii_lowercase
        if count < len(base): return (base)[count]
        else: return GetCountName36(count // len(base)) + (base)[count % len(base)]

    # count値とfiles数が一致した時（ディレクトリ配下がすべてこのツールで作成された名前のファイルと思われるとき）
    def __Alignment(self, count):
        if self.__args.alignment and count == len(self.__files):
            fig = (math.log(count, self.__args.radix) + 1)
            if 10 == self.__args.radix or 16 == self.__args.radix or 36 == self.__args.radix:
                self.__AppendAlignment('0'*fig)
            elif 26 == self.__args.radix:
                self.__AppendAlignment('a'*fig)
    def __AppendAlignment(self, prefix):
        import os
        for f in self.__files:
            d = os.path.dirname(f)
            name, ext = os.path.splitext(os.path.basename(f))
            name = prefix + name
            os.rename(f, os.path.join(d, name+ext))


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

