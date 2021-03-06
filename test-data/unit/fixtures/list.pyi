# Builtins stub used in list-related test cases.

from typing import TypeVar, Generic, builtinclass, Iterable, Iterator, overload

T = TypeVar('T')

@builtinclass
class object:
    def __init__(self): pass

class type: pass
class ellipsis: pass

class list(Iterable[T], Generic[T]):
    @overload
    def __init__(self) -> None: pass
    @overload
    def __init__(self, x: Iterable[T]) -> None: pass
    def __iter__(self) -> Iterator[T]: pass
    def __add__(self, x: list[T]) -> list[T]: pass
    def __mul__(self, x: int) -> list[T]: pass
    def __getitem__(self, x: int) -> T: pass
    def append(self, x: T) -> None: pass
    def extend(self, x: Iterable[T]) -> None: pass

class tuple: pass
class function: pass
class int: pass
class str: pass
class bool: pass

property = object() # Dummy definition.
