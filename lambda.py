def add_five(x):
    return x + 5

add_five_lambda = lambda x: x + 5

print(f"Def output: {add_five(10)}")
print(f"Lambda output: {add_five_lambda(10)}")

numbers = [1, 2, 3, 4, 5, 6]
cubed = list(map(lambda x: x**3, numbers))
print(f"Cubed: {cubed}") 
filtered = list(filter(lambda x: x > 3, numbers))
print(f"Filtered: {filtered}")


