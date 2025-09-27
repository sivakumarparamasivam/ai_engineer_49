def add(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add(10, 20))


def add(**args):
    total = 0
    for key, value in args.items():
        print(f"{key}: {value}")
        total += value
    return total
print(add(a=10, b=20, c=30))