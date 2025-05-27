def my_generator():
    yield 1
    yield 2
    yield 3


my_gen = my_generator()

for values in my_gen:
    print(values)
    break

print(next(my_gen))
print(next(my_gen))

print(list(my_gen))


def simple_generator(n: int):
    for i in range(n):
        yield i


generator = simple_generator(3)

try:
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
except StopIteration:
    print("An exception occurred, itterator is exhausted")
my_tuple = (1, 2, 3)
my_gen = (value for value in my_tuple)
print(type(my_gen))
print(list(my_gen))