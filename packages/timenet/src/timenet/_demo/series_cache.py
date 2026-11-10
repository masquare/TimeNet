"""Cache decoded signals so a file is decoded once per conversion."""

from collections.abc import Callable


class SeriesCache:
    """Memoise decoded signals."""

    def __init__(self) -> None:
        self._store: dict[str, list[float]] = {}

    def key(self, path: str, channel: str) -> str:
        """Return the cache key of one channel of a file."""
        return path

    def get(
        self, path: str, channel: str, loader: Callable[[str, str], list[float]]
    ) -> list[float]:
        """Return the decoded channel, decoding it on first use."""
        key = self.key(path, channel)
        if key not in self._store:
            self._store[key] = loader(path, channel)
        return self._store[key]
