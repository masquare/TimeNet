"""Size of fetched data."""

from collections.abc import Callable

from timenet._demo4.fetch import fetch_all


def total_bytes(urls: list[str], get: Callable[[str], bytes]) -> int:
    """Return the total size of all bodies.

    Returns:
        The number of bytes fetched.
    """
    return sum(len(body) for body in fetch_all(urls, get) if body)
