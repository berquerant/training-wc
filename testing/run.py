import json
import os
import random
import statistics
import string
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from functools import reduce
from typing import IO, Any, Callable, Generic, TypeVar

import pkommand


def json_dumps(obj: Any) -> str:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True)


HIRAGANA = "".join(chr(c) for c in range(0x3041, 0x3094 + 1))
KATAKANA = "".join(chr(c) for c in range(0x30A1, 0x30FA + 1))
DATA_SEED = string.printable + HIRAGANA + KATAKANA


def set_random_seed():
    random.seed(os.getenv("TRAINING_WC_RANDOM_SEED"))


def new_random_str(size: int, lines: int = 1) -> str:
    return "\n".join("".join(random.choices(DATA_SEED, k=size)) for _ in range(lines))


def generate(length: int):
    """
    Generate a random string.
    If environment variable TRAINING_WC_RANDOM_SEED is set, initalize the random number generator by it.
    """

    if length < 1:
        raise Exception("length should be positive")
    print(new_random_str(length))


T = TypeVar("T")


@dataclass
class Duration(Generic[T]):
    nano_sec: int
    result: T

    @staticmethod
    def measure(func: Callable[[], T]) -> "Duration[T]":
        t1 = time.monotonic_ns()
        r = func()
        t2 = time.monotonic_ns()
        return Duration(nano_sec=t2 - t1, result=r)


class WCResultError(Exception):
    pass


@dataclass
class WCResult:
    line: int
    word: int
    byte: int

    @classmethod
    def parse(cls, x: str) -> "WCResult":
        try:
            return cls.__parse(x)
        except Exception as e:
            raise WCResultError(f"Failed to parse {x}") from e

    @staticmethod
    def __parse(x: str) -> "WCResult":
        xs = x.split()
        if len(xs) != 3:
            raise Exception("Require 3 elements separated by spaces")
        return WCResult(
            line=int(xs[0]),
            word=int(xs[1]),
            byte=int(xs[2]),
        )

    def into_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class WCRunner:
    cmd: str
    stdin: IO | str

    def execute(self) -> str:
        kwargs: dict[str, Any] = {
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "check": True,
            "text": True,
        }
        if isinstance(self.stdin, str):
            kwargs["input"] = self.stdin
        else:
            kwargs["stdin"] = self.stdin
        return subprocess.run(
            self.cmd,
            **kwargs,
        ).stdout

    def run(self) -> WCResult:
        return WCResult.parse(self.execute())

    def run_with_timer(self) -> Duration[WCResult]:
        d = Duration.measure(self.execute)
        return Duration(nano_sec=d.nano_sec, result=WCResult.parse(d.result))


def run(cmd: str, timer: bool = False):
    """
    Run `cmd` equivalent to `wc` with stdin and parse result.
    If timer is True, measure `wc` duration.
    """

    if cmd == "":
        raise Exception("cmd required")

    runner = WCRunner(cmd=cmd, stdin=sys.stdin)

    def inner() -> dict[str, Any]:
        if not timer:
            return runner.run().into_dict()
        d = runner.run_with_timer()
        return {
            "duration_ns": d.nano_sec,
            **d.result.into_dict(),
        }

    print(json_dumps(inner()))


def accuracy(cmd: str, input_length: int, n: int, lines: int = 1):
    """
    Measure accuracy of command equivalent to wc.
    Run `cmd` equivalent to `wc` with random data `n` times.
    Input a random string with `lines` lines, a line length of `input_length` to `wc`.
    """

    if cmd == "":
        raise Exception("cmd required")
    if n < 1:
        raise Exception("n should be positive")
    if input_length < 1:
        raise Exception("input_length should be positive")
    if lines < 1:
        raise Exception("lines should be positive")

    original_wc_cmd = os.environ.get("TRAINING_WC_ORIGINAL", "wc")

    def test(data: str) -> dict[str, Any]:
        want = WCRunner(cmd=original_wc_cmd, stdin=data).run()
        got = WCRunner(cmd=cmd, stdin=data).run()
        return {
            "want": want.into_dict(),
            "got": got.into_dict(),
            "correct": want == got,
        }

    results = [test(new_random_str(input_length, lines)) for _ in range(n)]

    correct = reduce(
        lambda acc, x: acc + x["correct"],
        results,
        0,
    )

    print(
        json_dumps(
            {
                "results": results,
                "correct": correct,
                "incorrect": n - correct,
                "accuracy": correct / n,
                "n": n,
            }
        )
    )


def bench(cmd: str, input_length: int, n: int, lines: int = 1):
    """
    Measure execution time of command equivalent to wc.
    Run `cmd` equivalent to `wc` with random data `n` times.
    Input a random string with `lines` lines, a line length of `input_length` to `wc`.
    """

    if cmd == "":
        raise Exception("cmd required")
    if n < 1:
        raise Exception("n should be positive")
    if input_length < 1:
        raise Exception("input_length should be positive")
    if lines < 1:
        raise Exception("lines should be positive")

    runner = WCRunner(cmd=cmd, stdin=new_random_str(input_length, lines))
    raw_results = [runner.run_with_timer() for _ in range(n)]
    durations = [x.nano_sec for x in raw_results]
    print(
        json_dumps(
            {
                "results": durations,
                "max": max(durations),
                "min": min(durations),
                "mean": statistics.mean(durations),
                "stdev": statistics.stdev(durations),
            }
        )
    )


def main():
    set_random_seed()
    functions = [
        generate,
        run,
        bench,
        accuracy,
    ]
    runner = pkommand.Wrapper.default()
    for func in functions:
        runner.add(func)
    runner.run()


if __name__ == "__main__":
    main()
