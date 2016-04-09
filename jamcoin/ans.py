#!/usr/bin/env python


def print_coins(N, J):
    """Prints J jamcoins of length N each followed by 9 non trivial divisors."""
    pass


def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s:' % i+1
        print_coins(*map(int, raw_input().split()))


if __name__ == "__main__":
    main()
