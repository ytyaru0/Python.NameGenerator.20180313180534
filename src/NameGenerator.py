import glob
import os.path
import string
import math

# ファイル数から名前を生成する
class NameGenerator:
    def __init__(self, path_dir_target, extension, radix=36, is_alignment=True):
        self.__path_dir_target = path_dir_target
        self.__extension = extension
        self.__radix = radix
        self.__is_alignment = is_alignment
        self.__files = []
        if not os.path.isdir(self.__path_dir_target): raise Exception('存在するディレクトリのパスを指定して下さい。: {}'.format(self.__path_dir_target))
        
    @property
    def Characters(self):
        if 1 < self.__radix <= 10: return string.digits[:self.__radix]
        elif self.__radix < 26: return string.digits + string.ascii_lowercase[:self.__radix - len(string.digits)]
        elif self.__radix == 26: return string.ascii_lowercase
        elif self.__radix <= 36: return string.digits + string.ascii_lowercase[:self.__radix - len(string.digits)]
        elif self.__radix == 64: return string.digits + string.ascii_lowercase + string.ascii_uppercase + '_-'
        elif self.__radix == 85: return string.digits + string.ascii_lowercase + string.ascii_uppercase + "!#$%&'()-=~^@`[]{};+,._"
        raise Exception('radixが未対応値です。2〜36, 64, 85のいずれかの整数値にしてください。2〜36, 64, 85のいずれかの整数値にしてください。')

    def Generate(self):
        self.__GetFileNames()
        count = len(self.__files)
        name = self.__GetCountName(count)
        self.__Alignment(count)
        return name

    def __GetFileNames(self):
        reg = '*'
        if self.__extension is not None:
            if self.__extension.startswith('.'): reg += self.__extension
            else: reg += '.{}'.format(self.__extension)
        self.__files.clear()
        for path in glob.glob(os.path.join(self.__path_dir_target, reg)):
            if self.__extension is None:
                if os.path.isdir(path): self.__files.append(os.path.basename(path))
            else:
                if os.path.isfile(path): self.__files.append(os.path.splitext(os.path.basename(path))[0])
        sorted(self.__files)

    def __GetCountName(self, count:int):
        chars = self.Characters
        if count < len(chars): return (chars)[count]
        else: return self.__GetCountName(count // len(chars)) + (chars)[count % len(chars)]

    # 10.pyの名前が出力された直後、0.pyを00.pyとしたい
    def __Alignment(self, count):
        if self.__is_alignment and (count == len(self.__files)):
            import os
            prefix = self.Characters[0]
            for name in self.__files:
                fig = math.floor(math.log(count, self.__radix)) + 1
                if self.__extension: ext = '.' + self.__extension
                else: ext = ''
                os.rename(
                    os.path.join(self.__path_dir_target, name+ext), 
                    os.path.join(self.__path_dir_target, prefix*(fig - len(name)) + name+ext))
