
a = [1, 3, 5, 7]
it = iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

exit()

# yield
def frange(x, y, z):
    while x < y:
        yield x
        x += z


for i in frange(10, 20, 0.5):
    print(i)

