import os
print(os.path.abspath('.'))
print(os.path.exists('test.txt'))
print(os.path.isdir('test.txt'))
print(os.path.join('tmp/a/', 'b/c'))
print(type(os.path.join('tmp/a/', 'b/c')))


from pathlib import Path
p = Path('.')
print(p.resolve())
print(p.is_dir())

## mkdir
# q = Path('D:\\a\\b\\c')
# Path.mkdir(q, parents=True)
