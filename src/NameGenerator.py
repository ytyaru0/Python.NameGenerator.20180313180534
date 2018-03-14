import glob
import os.path
import string
import math

class NameGenerator:
    def __init__(self, args):
        self.__args = args
        self.__files = []
        if not os.path.isdir(self.__args.path_dir_target): raise Exception('存在するディレクトリのパスを指定して下さい。: {}'.format(self.__args.path_dir_target))
        self.__bases = {10: string.digits, 
                        16: string.digits + string.ascii_lowercase[:6],
                        26: string.ascii_lowercase,
                        36: string.digits + string.ascii_lowercase}

    def Generate(self):
        self.__GetFileNames()
        print(self.__files)
        count = self.__FindMin(0)
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
            self.__files.append(os.path.splitext(os.path.basename(path))[0])
        sorted(self.__files)

    def __FindMin(self, count:int):
        print('count:', count)
        for f in self.__files:
            if f == self.__GetCountName(count): return self.__FindMin((count+1))
        return count
        #self.__count = count
        #return self.__GetCountName(count)

    def __GetCountName(self, count:int):
        chars = self.__bases[self.__args.radix]
        if count < len(chars): return (chars)[count]
        else: return self.__GetCountName(count // len(chars)) + (chars)[count % len(chars)]

    """
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
    """

    # ※現状、やってしまうと次から0を返すようになってしまう
    # 10.pyの名前が出力された直後、0.pyを00.pyとしたい
    # count値とfiles数が一致した時（ディレクトリ配下がすべてこのツールで作成された名前のファイルと思われるとき）
    def __Alignment(self, count):
        print('Alignment', type(count))
        if self.__args.alignment and (count == len(self.__files)):
            if 10 == self.__args.radix or 16 == self.__args.radix or 36 == self.__args.radix:
                self.__AppendAlignment(count, '0')
            elif 26 == self.__args.radix:
                self.__AppendAlignment(count, 'a')

    def __AppendAlignment(self, count, prefix):
        import os
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

