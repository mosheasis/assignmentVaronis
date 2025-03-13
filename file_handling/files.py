class File:
    def __init__(self, path: str):
        self._path = path
        self._file = None

    def _open_file(self, op):
        _open_file = open(self._path, op)
        return _open_file

    def read(self):
        return self._open_file("r").readlines()

    def write(self, new_line: str):
        return self._open_file("w").write(new_line + '\n')

    def add_line(self, new_line: str):
        return self._open_file("a").write(new_line + '\n')

    def __exit__(self):
        self._file.close()
