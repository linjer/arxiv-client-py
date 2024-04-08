import logging

import feedparser  # type: ignore
import requests

from arxiv_client import Article, Query

logger = logging.getLogger(__name__)


class Client:
    """
    Python wrapper for the Arxiv API
    """

    base_search_url = "https://export.arxiv.org/api/query"
    """
    Base URL for Arxiv API
    """

    _session = requests.Session()

    def __init__(self) -> None:
        self._session.headers.update({"User-Agent": "arxiv-client-py"})

    # TODO: Consider support for the following
    #  1. Generator
    #  2. Advanced paging
    #  3. Consider async io
    def search(self, query: Query) -> list[Article]:
        """
        Search the Arxiv API

        :param query: The query to search with
        :return: The search results
        """
        logger.debug("Searching arxiv with query: %r", query)
        response = self._session.get(self.base_search_url, params=query._to_url_params())  # noqa: SLF001
        response.raise_for_status()

        feed = feedparser.parse(response.content)
        logger.debug("ArXiv returned %d results", len(feed.entries))
        return [Article.from_feed_entry(entry) for entry in feed.entries]
