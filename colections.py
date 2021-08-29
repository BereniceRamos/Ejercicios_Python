xs = [()]
res = [False]*2
# print(type(xs))
# print(res)
if xs:
    print(xs)
    print(f"Este es otro: {xs}")
    res[0] = True
    print(res)
if xs[0]:
    print(f"Este es: {xs[0]}")
    res[1] = True
    print(res)