import functools

res = functools.reduce(lambda x, y: x+y, range(10))
print(res)
c = filter(lambda n:n>2, range(10))
for x in c:
    print(x)