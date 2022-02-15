def func1(a,b):
    if a == b:
        return a
    else:
        if a<b:
            return func1(a, b-a)
        else:
            return func1(a-b, b)

print(func1(21,14))
