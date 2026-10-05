import pytest
from pydantic import HttpUrl

from dina.matcher.main import Matcher


@pytest.mark.parametrize(
    ("uris", "expected"),
    [
        pytest.param([], True, id="empty-filter"),
        pytest.param(["https://example.com/"], True, id="exact-origin"),
        pytest.param(["https://example.com/device/123"], True, id="child-url"),
        pytest.param(["https://other.example.com/device/123"], False, id="other-origin"),
        pytest.param(["http://example.com/"], False, id="other-scheme"),
        pytest.param(
            ["https://other.example.com/", "https://example.com/device/123"],
            True,
            id="matching-origin-after-unrelated-url",
        ),
    ],
)
def test_matches_origin(uris: list[str], expected: bool) -> None:
    assert Matcher._matches_origin([HttpUrl(uri) for uri in uris], HttpUrl("https://example.com/")) is expected
