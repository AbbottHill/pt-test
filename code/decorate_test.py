
def dec2(p):
    def tips2(func):
        def info2(a, b):
            print('param is %s and function name is %s' %(p, func.__name__))
            print(a)
            func(a, b)
            print(b)

        return info2
    return tips2


@dec2('my dec test')
def sub(a, b):
    print(a - b)


sub(0, 2)

#################################################


def tips(func):
    def info(a, b):
        print('%s' % func.__name__)
        print(a)
        func(a, b)
        print(b)

    return info


@tips
def add(a, b):
    print(a + b)


add(1, 2)
