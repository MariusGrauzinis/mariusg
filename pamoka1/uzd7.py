class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_title(self) -> str:
        return f"Name: {self.title}"

    def get_author(self) -> str:
        return f"Author: {self.author}"

pride_and_prejudice = Book("Puikybė ir prietarai", "Džeinė Ostin")
hamlet = Book("Hamletas", "Viljamas Šekspyras")
war_and_peace = Book("Karas ir taika", "Levas Tolstojus")
harry_potter = Book("Haris Poteris", "D. K. Rouling")

print(harry_potter.get_title())  
print(harry_potter.get_author())  

print(pride_and_prejudice.get_title())  
print(pride_and_prejudice.get_author())  

print(hamlet.get_title())  
print(hamlet.get_author())  

print(war_and_peace.get_title())  
print(war_and_peace.get_author())  