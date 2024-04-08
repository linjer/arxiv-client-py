from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import feedparser


@dataclass(init=True, repr=True, eq=True)
class Link:
    """
    Link to an article
    """

    title: str | None
    """
    The title of the link
    """
    href: str
    """
    The URL of the link
    """
    rel: str | None
    """
    The relation of the link. Can be alternate or related
    """
    mime_type: str | None
    """
    MIME type of the entity being linked, e.g., text/html
    """

    def __str__(self) -> str:
        return self.href

    @staticmethod
    def from_feed_link(link: feedparser.FeedParserDict) -> Link:
        """
        Create a Link object from a feedparser link entry

        :param link: The feedparser link entry
        :return: The Link object
        """
        title = link.get("title")
        href = link["href"]
        rel = link.get("rel")
        mime_type = link.get("type")
        return Link(title, href, rel, mime_type)
