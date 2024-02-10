class Author:
    def __init__(self, name:str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

class Book:
    def __init__(self, author:Author, title: str, pages: int, literary_genre: str | None = None) -> None:
        self.title = title
        self.pages = pages
        self.literary_genre = literary_genre

    def __str__(self):
        return f"{self.title} by {self.author}"
