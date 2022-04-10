'''
calculate how many bottles of beer you can drink.
no sence
'''


def bottles_cnt_beer(money=10):
    price = 2
    m = 3   # m empty bottles --> 1 bottle of beer
    count = money / price
    empty_cnt = money / price
    while empty_cnt >= m:
        count += empty_cnt / m
        empty_cnt = (empty_cnt / m) + (empty_cnt % m)
    return count

if __name__ == '__main__':
    n = int(raw_input('Enter a number: '))
    print "you can drink %d bottles of beer." % bottles_cnt_beer(n)
