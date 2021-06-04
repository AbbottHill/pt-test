def a_line(a, b):
    def cal(x):
        return a * x + b

    return cal


cal1 = a_line(1, 1)
cal2 = a_line(2, 2)
print(cal1(1))
print(cal2(2))
