"""Window positions over a sample array."""


def window_bounds(n: int, size: int, stride: int) -> list[tuple[int, int]]:
    """Return the (start, stop) pair of each full window over ``n`` samples.

    ``stop`` is the index of the last sample in the window.
    """
    return [(start, start + size - 1) for start in range(0, n - size + 1, stride)]
