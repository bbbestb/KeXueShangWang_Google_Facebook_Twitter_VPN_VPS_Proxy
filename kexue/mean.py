####
import numpy

def mean(numbers):
    ''' calculate the mean value of a number list '''
    return float(sum(numbers)) / max(len(numbers), 1)


if __name__ == '__main__':
    list1 = [134, 134, 34.324, 34354, 11.2]
    print mean(list1)
    print numpy.mean(list1)
