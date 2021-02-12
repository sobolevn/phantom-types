from typing import Container
from typing import Iterable
from typing import Sized

from phantom.base import Predicate


def contains(value: object) -> Predicate[Container]:
    """Create a predicate that succeeds when its argument contains ``value``."""

    def check(container: Container) -> bool:
        return value in container

    return check


def contained(container: Container) -> Predicate[object]:
    """Create a predicate that succeeds when ``container`` contains it."""

    def check(value: object) -> bool:
        return value in container

    return check


def count(predicate: Predicate[int]) -> Predicate[Sized]:
    """
    Create a predicate that succeeds when the size of its argument satisfies
    ``predicate``.
    """

    def check(sized: Sized) -> bool:
        return predicate(len(sized))

    return check


def exists(predicate: Predicate[object]) -> Predicate[Iterable]:
    """
    Create a predicate that succeeds given an iterable where one or more items satisfy
    ``predicate``.
    """

    def check(iterable: Iterable) -> bool:
        return any(predicate(item) for item in iterable)

    return check


def every(predicate: Predicate[object]) -> Predicate[Iterable]:
    """
    Create a predicate that succeeds given an iterable where all items satisfy
    ``predicate``.
    """

    def check(iterable: Iterable) -> bool:
        return all(predicate(item) for item in iterable)

    return check
