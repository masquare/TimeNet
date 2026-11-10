"""Cache decoded signals so a file is decoded once per conversion."""

from collections.abc import Callable


class SeriesCache:
    """Memoise decoded signals."""

    def __init__(self) -> None:
        self._store: dict[tuple[str, str], list[float]] = {}

    def get(self, path: str, channel: str, loader: Callable[[str, str], list[float]]) -> list[float]:
        """Return the decoded channel, decoding it on first use."""
        key = (path, channel)
        if key not in self._store:
            self._store[key] = loader(path, channel)
        return self._store[key]
