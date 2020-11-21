numbers = [3, 4, 1, 2, 16, 27, 13]
numbers.sort(key=lambda x: x if x % 2 != 0 else 0)
b=[i for i in numbers if i%2]
e=[i for i in numbers if not i%2]
e.sort(reverse = False)
b.sort(reverse=True)


print(e,b)

