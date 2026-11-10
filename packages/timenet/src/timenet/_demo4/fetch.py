"""Fetch many resources."""

from collections.abc import Callable

from timenet._demo4.retry import call_with_retry


def fetch_all(urls: list[str], get: Callable[[str], bytes]) -> list[bytes | None]:
    """Fetch every url, retrying each one.

    Returns:
        The body of each url, in order.
    """
    return [call_with_retry(lambda url=url: get(url)) for url in urls]
