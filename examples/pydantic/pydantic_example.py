from __future__ import annotations

import datetime
import re

from phantom.datetime import TZAware
from phantom.interval import Natural
from phantom.predicates.interval import closed_open
from phantom.re import Match
from phantom.sized import PhantomSized
from pydantic import BaseModel


class Name(str, PhantomSized[str], len=closed_open(0, 20)):
    ...


class Email(Match, pattern=re.compile(r"^[a-z._]+@[a-z\-]+\.(?:com|se|am)$")):
    ...


class Author(BaseModel):
    name: Name
    email: Email


class Book(BaseModel):
    id: Natural
    name: Name
    published: TZAware
    author: Author


book = Book.parse_obj(
    {
        "id": 1,
        "name": "foo",
        "published": datetime.datetime.now(tz=datetime.timezone.utc),
        "author": {"name": "Jane Doe", "email": "jane@doe.com"},
    }
)
assert isinstance(book, Book)
print(f"{book=}")

# Yeay, multiple errors :)))
Book.parse_obj(
    {
        "id": 1,
        "name": "foo",
        # "published": datetime.datetime.now(tz=datetime.timezone.utc),
        "published": "lol",
        # "published": datetime.datetime.now(),
        "author": {"name": "Jane Doe is a very very long name", "email": "jane@doe.com"},
    }
)

# print(f"{book.schema_json(indent=2)}")
