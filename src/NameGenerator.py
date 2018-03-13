import glob

class NameGenerator:
    def __init__(self, path):
        self.__path = path
        self.__files = []
        if not os.path.isdir(path): raise Exception('存在するディレクトリのパスを指定して下さい。: {}'.format(path))

    def Generate(self, ext=None):
        self.__GetFileNames(ext)
        return self.__FindMin(0)

    def __GetFileNames(self, ext):
        reg = '*'
        if ext is not None:
            if ext.startswith('.'): reg += ext
            else: reg += '.{}'.format(ext)
        self.__files.clear()
        for path in glob.glob(self.__path, reg):
            self.__files.append(os.path.splitext(os.path.basename(path))[0])
        sorted(self.__files)

    def __FindMin(self, count:int):
        for f in self.__files:
            if f == self.__GetCountName(count): self.__FindMin((count+1))
        return self.__GetCountName(count)

    def __GetCountName(self, count:int):
        if -1 < count and count < 10: return str(count)
        elif 9 < count and count < 37: return chr(97 + (count - 10))
        else: raise Exception('未実装。count={}以上の値でファイル名を作れません。'.format(count))


if __name__ == '__main__':
    import sys
    print(NameGenerator(sys.argv[0]).Generate(sys.argv[1]))

