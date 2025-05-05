# Sprint_4

### Тесты

#### 1.`test_add_new_book_with_valid_length_list_full_with_new_book`

**Проверка**: Проверка, что книга добавляется в список, если её название имеет длину, которая не превышает допустимую (от 1 до 40 символов).
Тест параметризирован: проврка идет по граничным значениям '1', '39' и '40' символов.

#### 2.`test_add_new_book_with_more_than_40_symbols_do_not_add_book_to_dict`

**Проверка**: Негативный сценарий проверки метода `add_new_book` - 
при привышении лимита 40 символов книга не будет добавлена в список

#### 3. `test_set_book_genre_from_genre_list_update_book_genre`

**Проверка**: Проверка присвоения книге жанра, если был передан жанр из списка доступных

#### 4. `test_set_book_genre_not_from_list_do_not_update_book_genre`

**Проверка**: Проверка НЕ присвоения книге жанра, если был передан жанр из списка доступных

#### 5. `test_get_book_genre_for_book_with_assigned_genre`

**Проверка**: Проверка получения жанра по имени книги, если он для нее установлен

#### 6. `def test_get_books_with_specific_genre_when_books_in_genre_exists`

**Проверка**: При условии наличии книги с определённым жанром,
метод возвращает её в списке книг с этим жанром.

#### 7. `test_get_books_with_specific_genre_when_books_in_genre_not_exists`
**Проверка**:

#### 8.  `test_get_books_genre_return_actual_info_from_dict`
**Проверка**: Получение актуального состояния списка

#### 9.    `test_get_books_for_children_approved_them`
**Проверка**: Проверка, что книги, подходящих для детей жанров будут добавлены в список.

#### 10.    `test_get_books_for_children_not_approved_them`
**Проверка**: Проверка, что книги жанров, которые недоступны детям не будут выведены в 
запрощенном списке

#### 11.    `test_add_book_in_favorites_if_book_name_in_list`
**Проверка**: Добавление книги в избранное, если книга с таким именем существует в списке книг

#### 12.    `get_list_of_favorites_books_when_no_books_added`
**Проверка**: Получение пустого списка с "избранным", если список избранного пуст

#### 13.    `test_delete_book_from_favorites_when_book_is_in_favorites`
**Проверка**: Удаление книги из списка "избранных", если в избранном есть добавленные книги
