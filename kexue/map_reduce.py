#!/usr/bin/python
# python built-in map()/reduce() exercises.

print map(lambda x: x.title(), ['adam', 'LISA', 'barT', 'Jay'])


def prod(list1):
    return reduce(lambda x, y: x * y, list1)


list1 = xrange(1, 6)
print prod(list1)
