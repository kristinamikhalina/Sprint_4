import pytest

import data
from main import BooksCollector


@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    collector.books = data.books_names
    return collector