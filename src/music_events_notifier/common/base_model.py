import abc
from itertools import chain

from pydantic import BaseModel, Extra


def to_camel(string: str) -> str:
    words = string.split("_")
    result = words[0]
    if len(words) > 1:
        result += "".join(chain(word.capitalize() for word in words[1:]))
    return result


class Model(BaseModel, abc.ABC):
    class Config:
        # faux immutability
        frozen = True
        # disallow setting extra attributes
        extra = Extra.forbid


class ViewModel(Model, abc.ABC):
    class Config:
        # for serializing to json
        alias_generator = to_camel
        allow_population_by_field_name = True
