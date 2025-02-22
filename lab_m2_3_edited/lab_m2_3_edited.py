class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Название: {self.name}, Автор: {self.author}"

    def __repr__(self):
        return f"Book(name='{self.name}', author='{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = pages

    def __str__(self):
        return f"{super().__str__()}, Количество страниц: {self.pages}"

    def __repr__(self):
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)) or duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = duration

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self.duration} часов"

    def __repr__(self):
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"







