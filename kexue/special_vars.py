#!/usr/bin/env python


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)


if __name__ == '__main__':
    jay = Student('Jay', 99)
    jay.print_score()
    #print jay.__name
    print jay._Student__name
