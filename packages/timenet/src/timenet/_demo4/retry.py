"""Retry flaky calls."""

from collections.abc import Callable
from typing import TypeVar


T = TypeVar("T")


def call_with_retry(fn: Callable[[], T], attempts: int = 3) -> T | None:
    """Call ``fn`` until it succeeds or ``attempts`` run out.

    Returns:
        The result of ``fn``.
    """
    result = None
    for _ in range(attempts):
        try:
            result = fn()
            break
        except Exception as error:
            print(f"retrying after {error}")
    return result
