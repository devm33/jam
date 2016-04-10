#!/usr/bin/env python

import math

def coin_value_in_base(base, coin):
    """Return coin value in base."""
    value = 0
    multiplier = 1
    for i, v in reversed(list(enumerate(coin))):
        if v:
            value += multiplier
        multiplier *= base
    return value

def check_base(base, coin):
    """Return divisor in base or False if prime."""
    value = coin_value_in_base(base, coin)
    if value % 2 == 0:
        return 2
    if value % 3 == 0:
        return 3
    div = 5
    while div * div < value:
        if value % div == 0:
            return div
        if value % (div + 2) == 0:
            return div + 2
        div += 6
    return False


def coins_iter(N):
    """Return an iterables of jamcoins length N."""
    for i in range(2**(N-2)):
        yield [True]+[0 != i & (2**bmap) for bmap in range(N-3, -1, -1)]+[True]

def print_coin(coin):
    return ''.join(map(str,map(int, coin)))

def print_coins(N, J):
    """Prints J jamcoins of length N each followed by 9 non trivial divisors."""
    count = 0
    for coin in coins_iter(N):
        out = []
        for base in range(2, 11):
            divisor = check_base(base, coin)
            if divisor:
                out.append(divisor)
            else:
                break
        if len(out) == 9:
            print '%s %s' % (print_coin(coin), ' '.join(map(str, out)))
            count += 1
            if count == J:
                return


def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s:' % (i+1)
        print_coins(*map(int, raw_input().split()))


if __name__ == "__main__":
    main()
