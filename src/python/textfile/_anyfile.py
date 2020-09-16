#!/usr/bin/env python3

from ._util import *


@dataclass
class AnyFile(AnyStr):
    filename: PathLike
    _path: Path = None
    _name: str = ''
    _size: int = 0
    _data: Union[str, bytearray, bytes, memoryview, mmap] = None
    _lines: List[Union[str, bytes]] = list

    def __post_init__(self) -> None:
        # if file does not exist, get rid of instance
        # # todo - find a better way ...
        if self.path is None:
            self.__del__()
            # del self
            raise AnyFileError(
                f'The path {self.filename} could not be located.')

    @property
    def short_name(self, filename: PathLike) -> str:
        _ = Path(filename).resolve()
        return f"..{self.parent.name}{self.name}"

    @property
    def path(self) -> Path:
        """ lazy determine and return path of file. """
        if not self._path:
            self._path = Path(self.filename).resolve()
        return self._path

    @property
    def parent(self) -> Path:
        """ lazy determine and return parent of file. """
        return self.path.parent

    @property
    def name(self) -> str:
        if not self._name:
            self._name = self.path.name
        return self._name
