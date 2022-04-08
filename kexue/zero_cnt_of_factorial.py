'''
calculate how many zero(0)s in the end of n!.
'''


def zero_cnt_of_factorial(num=50):
    count = 0
    i = 5
    while ((num / i) >= 1):
        count += num/i
        i *= 5
    return count

if __name__ == '__main__':
    n = int(raw_input('Enter a number: '))
    print "%d! has %d zeros in the end." % (n, zero_cnt_of_factorial(n))
