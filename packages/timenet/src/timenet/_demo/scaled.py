"""Read channels scaled to physical units."""

from collections.abc import Callable

from timenet._demo.series_cache import SeriesCache


def read_scaled(
    cache: SeriesCache,
    path: str,
    channel: str,
    gain: float,
    loader: Callable[[str, str], list[float]],
) -> list[float]:
    """Return the samples of one channel multiplied by ``gain``."""
    samples = cache.get(path, channel, loader)
    for i in range(len(samples)):
        samples[i] *= gain
    return samples
