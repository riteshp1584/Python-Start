tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

for num, letter in zip(tuple1, tuple2):
    print(num, letter)

numbers = [1, 2, 3, 4, 5]

func = (lambda x: x ** 3)

cubed = map(func, numbers)

print(list(cubed))

def sum_of_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total

print(sum_of_numbers(1, 2, 3, 4, 5, 6))

def print_info(name, age, **added):
    print(f"Name: {name}")
    print(f"Age: {age}")
    for key, value in added.items():
        print(f"{key}: {value}")

print_info(name="Raman", age=30, city="Bengaluru", job="Quant Analyst")

squares = {x:x**2 for x in range(1, 11)}

print(squares)

evens_squared = {x:x**2 for x in range(1, 11) if x % 2 == 0}

print(evens_squared)
