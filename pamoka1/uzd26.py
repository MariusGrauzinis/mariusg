from dataclasses import dataclass, field

@dataclass
class MediaItem:
    title: str
    creator: str
    year_published: int
    media_type: str = field(default="Unknown", init=False)

    def __post_init__(self):

        pass

@dataclass
class Book(MediaItem):
    number_of_pages: int
    author: str = field(init=False)

    def __post_init__(self):
        self.media_type = "Book"
        self.author = self.creator

@dataclass
class Movie(MediaItem):
    duration: int
    director: str = field(init=False)

    def __post_init__(self):
        self.media_type = "Movie"
        self.director = self.creator

@dataclass
class Album(MediaItem):
    number_of_tracks: int
    artist: str = field(init=False)

    def __post_init__(self):
        self.media_type = "Album"
        self.artist = self.creator



book = Book(title="1984", creator="George Orwell", year_published=1949, number_of_pages=328)
movie = Movie(title="Inception", creator="Christopher Nolan", year_published=2010, duration=148)
album = Album(title="Thriller", creator="Michael Jackson", year_published=1982, number_of_tracks=9)

print(book)
print(movie)
print(album)
