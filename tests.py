import pytest

from conftest import collector_with_books
from data import books_names
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize(
        "book_name",
        [
        "A",  # длина 1
        "A" * 39,  # длина 39
        "B" * 40  # длина 40
    ])
    def test_add_new_book_with_length_between_1_and_40_symbols_add_book_to_dict(self, collector_with_books, book_name):
        books_before = len(collector_with_books.get_books_genre())
        collector_with_books.add_new_book(books_names[1])
        assert len(collector_with_books.get_books_genre()) > books_before

    def test_add_new_book_with_more_than_40_symbols_do_not_add_book_to_dict(self, collector_with_books):
        long_book_name = 'K'*41
        collector_with_books.add_new_book(long_book_name)
        assert long_book_name not in collector_with_books.get_books_genre()


    def test_set_book_genre_from_genre_list_update_book_genre(self, collector_with_books):
        collector_with_books.add_new_book(books_names[0])
        collector_with_books.set_book_genre(books_names[0], "Детективы")
        genre = collector_with_books.get_book_genre(books_names[0])
        assert genre == "Детективы"

    def test_set_book_genre_not_from_list_do_not_update_book_genre(self, collector_with_books):
        collector_with_books.add_new_book(books_names[0])
        collector_with_books.set_book_genre(books_names[0], "Триллеры")
        genre = collector_with_books.get_book_genre("Преступление и наказание")
        assert not genre == "Ужасы"


    def test_get_book_genre_for_book_with_assigned_genre(self, collector_with_books):
        collector_with_books.add_new_book(books_names[0])
        collector_with_books.set_book_genre(books_names[0], "Детективы")
        genre = collector_with_books.get_book_genre(books_names[0])
        assert genre == "Детективы"


    def test_get_books_with_specific_genre_when_books_in_genre_exists(self, collector_with_books):
        collector_with_books.add_new_book(books_names[2])
        collector_with_books.set_book_genre(books_names[2], "Фантастика")
        assert collector_with_books.get_books_with_specific_genre('Фантастика') == [books_names[2]]

    def test_get_books_with_specific_genre_when_books_in_genre_not_exists(self, collector_with_books):
        collector_with_books.add_new_book(books_names[2])
        collector_with_books.set_book_genre(books_names[2], "Фантастика")
        assert collector_with_books.get_books_with_specific_genre('Мультфильмы') == []


    def test_get_books_genre_return_actual_info_from_dict(self, collector_with_books):
        collector_with_books.add_new_book(books_names[3])
        collector_with_books.set_book_genre(books_names[3], "Мультфильмы")
        assert collector_with_books.get_books_genre() == {books_names[3]: "Мультфильмы"}


    def test_get_books_for_children_approved_them(self, collector_with_books):
        collector_with_books.add_new_book(books_names[3])
        collector_with_books.set_book_genre(books_names[3], "Мультфильмы")
        assert collector_with_books.get_books_for_children() == [books_names[3]]

    def test_get_books_for_children_not_approved_them(self, collector_with_books):
        collector_with_books.add_new_book(books_names[4])
        collector_with_books.set_book_genre(books_names[4], "Ужасы")
        assert collector_with_books.get_books_for_children() == []


    def test_add_book_in_favorites_if_book_name_in_list(self, collector_with_books):
        collector_with_books.add_new_book(books_names[4])
        collector_with_books.add_book_in_favorites(books_names[4])
        assert collector_with_books.get_list_of_favorites_books() == [books_names[4]]

    def get_list_of_favorites_books_when_no_books_added(self,collector_with_books):
        assert collector_with_books.get_list_of_favorites_books() == []


    def test_delete_book_from_favorites_when_book_is_in_favorites(self, collector_with_books):
        collector_with_books.add_new_book(books_names[4])
        collector_with_books.add_book_in_favorites(books_names[4])
        collector_with_books.delete_book_from_favorites(books_names[4])
        assert collector_with_books.get_list_of_favorites_books() == []

