# -*- coding: utf-8 -*-

from collections import defaultdict

colors = ['red', 'green', 'white', 'red', 'blue', 'red']

d = {}
for c in colors:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d1 = {}
for c in colors:
    d1[c] = d1.get(c, 0) + 1
print(d1)

d2 = defaultdict(int)
for c in colors:
    d2[c] += 1
print(d2)


from collections import OrderedDict
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys()) # 按照插入的Key的顺序返回


from collections import deque

# 双端队列
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


from collections import Counter
c = Counter()
for ch in 'helloworld':
    c[ch] = c[ch] + 1
print(c)