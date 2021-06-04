
s = input("input sth: ")

print(s, type(s))

s = int(input("input sth: "))
print(s, type(s))


class A:
    pass


class B(A):
    pass


print(type(A()) == A)
print(type(B) == A)
print(isinstance(A(), A))
print(isinstance(B(), A))
