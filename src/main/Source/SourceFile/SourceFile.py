import abc
from Source import Source

class SourceFile(Source,metaclass=abc.ABCMeta):

    def __init__(self, path,file_name):
        self._path = path
        self._file_name = file_name
