animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals, key=len, reverse=True))


# def reverse(s: str):
#     return s[::-1]


reverse = lambda s: s[::-1]

print(reverse("Hello"))
print((lambda s: s[::-1])("I am a string"))