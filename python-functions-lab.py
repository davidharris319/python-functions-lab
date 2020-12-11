# Exercise 1

print('Exercise 1')


def sum_to(n):
    total = 0
    for num in range(1, n + 1):
        total += num

    return total


print(sum_to(6))
print(sum_to(10))

# Exercise 2

print('Exercise 2')


def largest(list):
    largest_num = 0
    for num in list:
        if num > largest_num:
            largest_num = num

    return largest_num


print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231


# Exercise 3

print('Exercise 3')


def occurances(string1, string2):
    return string1.count(string2)


print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))   # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0

# Exercise 4

print('Exercise 4')


def product(*args):
    result = 1
    for n in args:
        result *= n
    return result


print(product(-1, 4))  # returns -4
print(product(2, 5, 5))  # returns 50
print(product(4, 0.5, 5))  # returns 10.0
