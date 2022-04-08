#!/usr/bin/python
# test how to use for-else / while-else clause.
# else sub-clause will be executed when there's no break/return/exception in the
# iteration.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

for i in list1:
    if i > 5:
        print 'item is larger than 5; the index in list1 is %d' % list1.index(i)
        break
else:
    print 'No item in list1 is larger than 5.'

for i in list2:
    if i > 5:
        print 'item is larger than 5; the index in list2 is %d' % list2.index(i)
        break
else:
    print 'No item in list2 is larger than 5.'


i = 0
while i < 10:
    if i > 5:
        print '%d is larger than 5' % i
        break
    i += 1
else:
    print 'No one is larger than 5'
