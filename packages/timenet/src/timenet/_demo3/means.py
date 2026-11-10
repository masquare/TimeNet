"""Summaries of windowed samples."""

from collections.abc import Sequence

from timenet._demo3.slicer import take_windows


def window_means(samples: Sequence[float], size: int, stride: int) -> list[float] | None:
    """Return the mean of each full window."""
    if not samples:
        return None
    return [sum(window) / len(window) for window in take_windows(samples, size, stride)]
