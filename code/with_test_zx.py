
class TestWith:
    def __enter__(self):
        print('run')
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('normal end')
        else:
            print('%s: %s' %(exc_val, exc_tb))


with TestWith():
    print('test is runing')
    # raise NameError('NameError test')


with open("test.txt") as f:
    for l in f.readlines():
        print(l)


