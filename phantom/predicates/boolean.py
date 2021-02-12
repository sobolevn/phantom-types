from typing import Iterable
from typing import Literal

from .base import Predicate
from .base import T


def true(_value: object) -> Literal[True]:
    """Always return ``True``."""
    return True


def false(_value: object) -> Literal[False]:
    """Always return ``False``."""
    return False


def negate(p: Predicate[T]) -> Predicate[T]:
    """Negate a given predicate."""

    def check(value: T) -> bool:
        return not p(value)

    return check


def truthy(value: object) -> bool:
    """Return ``True`` given a truthy object."""
    return bool(value)


falsy = negate(truthy)
falsy.__doc__ = "Return ``True`` given a falsy object."


def both(p: Predicate[T], q: Predicate[T]) -> Predicate[T]:
    """Create a predicate that succeeds when both of the given predicates succeed."""

    def check(value: T) -> bool:
        return p(value) and q(value)

    return check


def all_of(predicates: Iterable[Predicate[T]]) -> Predicate[T]:
    """Creat a predicate that succeeds when all of the given predicates succeed."""
    predicates = tuple(predicates)

    def check(value: T) -> bool:
        return all(p(value) for p in predicates)

    return check


def any_of(predicates: Iterable[Predicate[T]]) -> Predicate[T]:
    """
    Create a new predicate that succeeds when at least one of the given predicates
    succeed.
    """
    predicates = tuple(predicates)

    def check(value: T) -> bool:
        return any(p(value) for p in predicates)

    return check
