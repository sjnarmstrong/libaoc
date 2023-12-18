import os
import re
import typing
import itertools
from functools import partial
from dataclasses import dataclass, field
from typing import Any


def get_puzzle(day = None, year=None):
    from aocd.models import Puzzle, default_user
    if day is None or year is None:
        matches = re.findall(r"/.?.?.?(20\d\d).?.?.?/.?.?.?([0-2]\d)", os.path.abspath("."))
        matches = matches[-1]
        day = day or int(matches[1])
        year = year or int(matches[0])
    user = default_user()
    return Puzzle(year=year, day=day, user=user)

def download_data(data_dir: str, day = None, year=None):
    if os.path.isfile(data_dir):
        return

    from aocd import get_data as aocd_get_data
    if day is None or year is None:
        matches = re.findall(r"/.?.?.?(20\d\d).?.?.?/.?.?.?([0-2]\d)", os.path.abspath("."))
        if len(matches) == 0:
            print("could not infer date")
            return data
        matches = matches[-1]
        day = day or int(matches[1])
        year = year or int(matches[0])
    data = aocd_get_data(day=day, year=year)
    with open(data_dir, "w") as fp:
        fp.write(data)

def get_data(
    test_case: int, 
    test_data: typing.List[str], 
    data: str=None,
    skip_dl = False
) -> str:
    data = data or "./data.txt"
    if not skip_dl: download_data(data)
    if test_case == -1:
        data = data
    else:
        if isinstance(test_data, str):
            test_data = [test_data]
        data = test_data[test_case]
    if os.path.isfile(data):
        with open(data, "r") as fp:
            return fp.read()
    else:
        return data


def get_ints(value: str, keep_str: bool = False, per_ln: bool=False):
    val_itr = value.splitlines() if per_ln else [value]
    out = []
    for val in val_itr:
        v = re.findall(r"[-+]?\d+", val)
        if keep_str:
            out.append(v)
        else:
            out.append([int(vi) for vi in v])
    return out if per_ln else out[0]


def get_floats(value: str, keep_str: bool = False, per_ln: bool=False):
    val_itr = value.splitlines() if per_ln else [value]
    out = []
    for val in val_itr:
        v = re.findall(r"[\d\.]+", val)
        if keep_str:
            out.append(v)
        else:
            out.append([float(vi) for vi in v])
    return out if per_ln else out[0]

class Unset:
    pass
class Skip:
    pass

@dataclass
class Convert:
    map_vals: dict=field(default_factory=dict)
    map_constructor: dict=field(default_factory=dict)
    map_default: typing.Any = Skip
    iterate: bool = True


    def convert_itr(self, values: str):
        if not self.iterate:
            values = [values]
        
        for value in values:
            if value in self.map_vals:
                yield self.map_vals[value]
                continue
            if value in self.map_constructor:
                yield self.map_vals[value](value)
                continue
            try:
                yield int(value)
                continue
            except ValueError:
                pass
            try:
                yield float(value)
                continue
            except ValueError:
                pass
            if self.map_default is Unset:
                yield value
                continue
            if self.map_default is Skip:
                continue
            yield self.map_default

    def __call__(self, values: str):
        out = list(self.convert_itr(values))
        if not self.iterate:
            if len(out) == 1:
                out = out[0]
            elif len(out) == 0:
                out = None
        return out


class Apply():
    def __init__(
        self,
        fn: typing.Union[typing.Callable, typing.Iterable],
        *args: typing.Any,
        **kwargs: typing.Any
    ):
        if callable(fn):
            fn = itertools.repeat(fn)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def __call__(
        self, 
        iter_v: typing.Iterable, 
    ) -> Any:
        return [f(v, *self.args, **self.kwargs) for v, f in zip(iter_v, self.fn)]


@dataclass
class Chain:
    fns: typing.Iterable[typing.Callable]
    def __call__(self, value: typing.Any):
        for f in self.fns:
            value = f(value)
        return value

@dataclass
class Split:
    by: str = field(default="\n")
    def __call__(self, value: str) -> typing.List[str]:
        return value.split(self.by)
    
@dataclass
class Strip:
    chars: typing.Optional[str] = None
    side: typing.Union[
        typing.Literal['l'],
        typing.Literal['r'],
        typing.Literal['b']
    ] = field(default="b")
    def __call__(self, value: str) -> typing.List[str]:
        if self.side == 'b':
            return value.lstrip(self.chars).rstrip(self.chars)
        if self.side == 'r':
            return value.rstrip(self.chars)
        if self.side == 'l':
            return value.lstrip(self.chars)
        
# TODO flatten and rollup