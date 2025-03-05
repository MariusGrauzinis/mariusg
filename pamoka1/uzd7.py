class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_title(self) -> str:
        return f"Name: {self.title}"

    def get_author(self) -> str:
        return f"Author: {self.author}"
    
    def book_info(self) -> str:
        return f"Name: {self.title}, Author: {self.author}"


dune = Book("Dune", " Frank Herbert")
no_longer_human = Book("No Longer Human", "Osamu Dazai")
normal_people = Book ("Normal People", "Sally Rooney")
the_songs_of_achilles = Book("The Song of Achilles", "Madeline Miller")
burn_after_writting = Book("Burn After Writing", "Sharon Jones")




print(dune.get_author())
print(the_songs_of_achilles.get_title())
print(normal_people.get_author())
print(no_longer_human.get_title())
print(the_songs_of_achilles.get_author())
print(burn_after_writting.get_title())
print(dune.book_info())
print(the_songs_of_achilles.book_info())