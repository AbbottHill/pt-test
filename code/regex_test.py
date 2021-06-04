import re


p = re.compile('\d+-\d+')
print(p.match('2021-06'))
print(p.match('2021-06aa').group())

# search
p_search = p.search('aaa2021-06bbb21-35sa')
print(p_search)

# findall
p_fall = p.findall('aaa2021-06bbb21-34')
print(p_fall)

# replace
re_sub = re.sub('\D', '', '2021年06月01日21:30:27')
print(re_sub)

