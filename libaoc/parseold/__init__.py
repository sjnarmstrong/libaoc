import types
import typing
import inspect


class ReadFile:
    def __call__(self, filename) -> typing.Any:
        with open(filename) as fp:
            return fp.read()


def finalize_generator(val):
    if isinstance(val, types.GeneratorType):
        return [v for v in val]
    return val


class Pipe:
    def __init__(self, *steps):
        self.steps = steps
    def __call__(self, *args):
        for s in self.steps:
            if isinstance(args, tuple):
                args = s(*args)
            else:
                args = s(*args)
            args = finalize_generator(args)
        return args


class TapeRecordedStr():
    def __init__(self, inner_str):
        self.last_idx = 0
        self.inner_str = inner_str
    def __getitem__(self, __key: typing.Union[typing.SupportsIndex, slice]) -> str:
        self.last_idx = max(self.last_idx, __key.stop)
        return self.inner_str.__getitem__(__key)

class Split:
    def __init__(self, *steps, repeat_on_end = True, on=None):
        self._steps = steps
        self.repeat_on_end = repeat_on_end
        self.on = on

    def steps(self):
        loop = True
        while loop:
            for step in self._steps:
                if isinstance(step, typing.Callable):
                    yield step
                else:
                    step, repeats = step
                    while repeats is None:
                        yield step
                    for _ in range(repeats): yield step
            loop = self.repeat_on_end

    def __call__(self, *args: typing.Any) -> typing.Any:
        step_itr = self.steps()
        for arg in args:
            if self.on is not None and isinstance(arg, str):
                for v, step in zip(args.split(self.on), step_itr):
                    yield step(v)
            else:
                while len(args) > 0:
                    args = TapeRecordedStr(str)
    