from colection.books import Author, Book

def test_book_str():
    jorge = Author("jorge")
    assert jorge.__str__() == "jorge"