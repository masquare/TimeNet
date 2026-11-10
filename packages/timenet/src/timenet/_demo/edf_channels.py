"""Read every channel of an EDF file through the shared cache."""

from collections.abc import Callable, Sequence

from timenet._demo.series_cache import SeriesCache


def read_channels(
    cache: SeriesCache,
    path: str,
    channels: Sequence[str],
    loader: Callable[[str, str], list[float]],
) -> dict[str, list[float]]:
    """Return the samples of each requested channel of one file."""
    return {channel: cache.get(path, channel, loader) for channel in channels}
