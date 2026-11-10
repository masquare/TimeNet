"""Cut a sample array into windows."""

from collections.abc import Sequence

from timenet._demo3.bounds import window_bounds


def take_windows(samples: Sequence[float], size: int, stride: int) -> list[Sequence[float]]:
    """Return the full windows of ``samples``."""
    bounds = window_bounds(len(samples), size, stride)
    return [samples[start:stop] for start, stop in bounds]
