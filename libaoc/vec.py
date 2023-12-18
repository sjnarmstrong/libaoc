import itertools
from typing import Iterable, Iterator, Dict, Callable
import math

class Vec:
    UP2: "Vec"
    DOWN2: "Vec"
    LEFT2: "Vec"
    RIGHT2: "Vec"
    UP3: "Vec"
    DOWN3: "Vec"
    LEFT3: "Vec"
    RIGHT3: "Vec"
    FORWARD3: "Vec"
    BACKWARD3: "Vec"
    COMMON_MAPPINGS_2: Dict[str,"Vec"]
    COMMON_MAPPINGS_3: Dict[str,"Vec"]
    def __init__(self, x=None,y=None,z=None,*args,D=None, other: 'Vec'=None)  -> None:
        if other is None:
            v = [
                (0 if a is None else a) 
                for i, a in enumerate(itertools.chain([x,y,z], args))
                if D is None or i<D
            ]
            if D is not None and len(v) < D:
                v.extend([0]*(D-len(v)))
            self.v = tuple(v)
        else:
            self.v = other.v

    @staticmethod
    def visualize_2d_vec_list(
        char_map: Dict[str, Iterable["Vec"]],
        other_char = ".",
    ):
        min_v = Vec.el_wise(
            itertools.chain(*char_map.values()),
            min
        )
        max_v = Vec.el_wise(
            itertools.chain(*char_map.values()),
            max
        )
        assert len(min_v) == 2
        vis_map = [
            [other_char for x in range(min_v[0], max_v[0])]
            for y in range(min_v[1], max_v[1])
        ]

        for c, vecs in char_map.items():
            for x,y in vecs:
                vis_map[y][x] = c
        return "".join(["".join(v) for v in vis_map])
        
    @staticmethod
    def UP(D=2):
        return Vec(0,1, D=D)
    @staticmethod
    def DOWN(D=2):
        return Vec(0,-1, D=D)
    @staticmethod
    def LEFT(D=2):
        return Vec(-1, 0, D=D)
    @staticmethod
    def RIGHT(D=2):
        return Vec(1,0, D=D)
    @staticmethod
    def FORWARD(D=3):
        return Vec(0,0,1, D=D)
    @staticmethod
    def BACKWARD(D=3):
        return Vec(0,0,-1, D=D)

    def copy(self) -> 'Vec':
        return Vec(other=self)
    
    @staticmethod
    def el_wise(vecs: Iterable["Vec"], fn: Callable) -> "Vec":
        return Vec(
            *(fn([v[el_idx] for v in vecs]) for el_idx, _ in enumerate(vecs[0]))
        )
    
    def __len__(self) -> int:
        return len(self.v)
    
    def __contains__(self, __o: object) -> bool:
        return __o in self.v
    
    def __iter__(self) -> Iterator:
        return iter(self.v)
    
    @staticmethod
    def _get_other_iter(__value: Iterable | object) -> Iterable:
        try:
            return iter(__value)
        except TypeError as te:
            return itertools.repeat(__value)
    
    def __trunc__(self):
        return Vec(*(math.trunc(vi) for vi in self))
    def __ceil__(self):
        return Vec(*(math.ceil(vi) for vi in self))
    def __floor__(self):
        return Vec(*(math.floor(vi) for vi in self))
    def __round__(self):
        return Vec(*(round(vi) for vi in self))

    def __invert__(self):
        return Vec(*(~vi for vi in self))
    def __abs__(self):
        return Vec(*(abs(vi) for vi in self))
    def __neg__(self):
        return Vec(*(-vi for vi in self))
    def __pos__(self):
        return Vec(*(+vi for vi in self))
    
    def __and__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1&vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rand__(self, __value: Iterable | object) -> "Vec":
        return self.__and__(__value)
    
    def __or__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1|vi2 for vi1, vi2 in zip(self,value_iter)))
    def __ror__(self, __value: Iterable | object) -> "Vec":
        return self.__or__(__value)
    
    def __xor__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1^vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rxor__(self, __value: Iterable | object) -> "Vec":
        return self.__xor__(__value)
    
    def __sub__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1-vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rsub__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2-vi1 for vi1, vi2 in zip(self,value_iter)))
    
    def __add__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1+vi2 for vi1, vi2 in zip(self,value_iter)))
    def __radd__(self, __value: Iterable | object) -> "Vec":
        return self.__add__(__value)
    
    def __mul__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1*vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rmul__(self, __value: Iterable | object) -> "Vec":
        return self.__mul__(__value)
    
    def __floordiv__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1//vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rfloordiv__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2//vi1 for vi1, vi2 in zip(self,value_iter)))
    
    def __div__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1/vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rdiv__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2/vi1 for vi1, vi2 in zip(self,value_iter)))
    
    def __truediv__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1/vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rtruediv__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2/vi1 for vi1, vi2 in zip(self,value_iter)))

    def __mod__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1%vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rmod__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2%vi1 for vi1, vi2 in zip(self,value_iter)))

    def __divmod__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(divmod(vi1,vi2) for vi1, vi2 in zip(self,value_iter)))
    def __rdivmod__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(divmod(vi2,vi1) for vi1, vi2 in zip(self,value_iter)))
    
    def __pow__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1**vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rpow__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2**vi1 for vi1, vi2 in zip(self,value_iter)))
    
    def __lshift__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1<<vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rlshift__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2<<vi1 for vi1, vi2 in zip(self,value_iter)))
    
    def __rshift__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi1>>vi2 for vi1, vi2 in zip(self,value_iter)))
    def __rrshift__(self, __value: Iterable | object) -> "Vec":
        value_iter = self._get_other_iter(__value)
        return Vec(*(vi2>>vi1 for vi1, vi2 in zip(self,value_iter)))
    
    def __le__(self, __value: "Vec") -> bool:
        return self.v <= __value.v
    def __lt__(self, __value: "Vec") -> bool:
        return self.v < __value.v
    def __ge__(self, __value: "Vec") -> bool:
        return self.v >= __value.v
    def __gt__(self, __value: "Vec") -> bool:
        return self.v > __value.v
    def __eq__(self, __value: "Vec") -> bool:
        return self.v == __value.v
    
    def __rle__(self, __value: "Vec") -> bool:
        return __value.v <= self.v
    def __rlt__(self, __value: "Vec") -> bool:
        return __value.v < self.v
    def __rge__(self, __value: "Vec") -> bool:
        return __value.v >= self.v
    def __rgt__(self, __value: "Vec") -> bool:
        return __value.v > self.v
    def __req__(self, __value: "Vec") -> bool:
        return __value.v == self.v
    
    def __hash__(self) -> int:
        return hash(self.v)
    
    def __str__(self) -> int:
        inner = ", ".join((str(vi) for vi in self.v))
        return f"<{inner}>"
    def __repr__(self) -> int:
        inner = ", ".join((repr(vi) for vi in self.v))
        return f"<{inner}>"

Vec.UP2 = Vec.UP(2)
Vec.DOWN2 = Vec.DOWN(2)
Vec.LEFT2 = Vec.LEFT(2)
Vec.RIGHT2 = Vec.RIGHT(2)

Vec.UP3 = Vec.UP(3)
Vec.DOWN3 = Vec.DOWN(3)
Vec.LEFT3 = Vec.LEFT(3)
Vec.RIGHT3 = Vec.RIGHT(3)
Vec.FORWARD3 = Vec.FORWARD(3)
Vec.BACKWARD3 = Vec.BACKWARD(3)

Vec.COMMON_MAPPINGS_2 = {
    "^": Vec.UP2,
    "v": Vec.DOWN2,
    "<": Vec.LEFT2,
    ">": Vec.RIGHT2,
    "u": Vec.UP2,
    "d": Vec.DOWN2,
    "l": Vec.LEFT2,
    "r": Vec.RIGHT2,
    "U": Vec.UP2,
    "D": Vec.DOWN2,
    "L": Vec.LEFT2,
    "R": Vec.RIGHT2,
    "w": Vec.UP2,
    "s": Vec.DOWN2,
    "a": Vec.LEFT2,
    "d": Vec.RIGHT2,
    "W": Vec.UP2,
    "S": Vec.DOWN2,
    "A": Vec.LEFT2,
    "D": Vec.RIGHT2,
}

Vec.COMMON_MAPPINGS_3 = {
    "^": Vec.UP3,
    "v": Vec.DOWN3,
    "<": Vec.LEFT3,
    ">": Vec.RIGHT3,
    "u": Vec.UP3,
    "d": Vec.DOWN3,
    "l": Vec.LEFT3,
    "r": Vec.RIGHT3,
    "f": Vec.FORWARD3,
    "b": Vec.BACKWARD3,
    "U": Vec.UP3,
    "D": Vec.DOWN3,
    "L": Vec.LEFT3,
    "R": Vec.RIGHT3,
    "F": Vec.FORWARD3,
    "B": Vec.BACKWARD3,
    "w": Vec.UP3,
    "s": Vec.DOWN3,
    "a": Vec.LEFT3,
    "d": Vec.RIGHT3,
    "W": Vec.UP3,
    "S": Vec.DOWN3,
    "A": Vec.LEFT3,
    "D": Vec.RIGHT3,
}