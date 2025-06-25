def reverse(s: str):
    return s[::-1]


animals = ["cat", "dog", "hedgehog", "gecko"]

print(reverse("Hello"))

my_answers = map(lambda s: s[::-1], animals)
print(list(my_answers))

my_answ = filter(lambda s: s > 3, animals)
print(list(my_answ))