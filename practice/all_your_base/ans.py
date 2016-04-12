#!/usr/bin/env python

def gen_values():
    yield 1
    yield 0
    n = 2
    while True:
        yield n
        n += 1

def min_secs(numstr):
    base = len(set(numstr))
    digits = {}
    value = gen_values()
    for d in numstr:
        if d not in digits:
            digits[d] = next(value)
    order = 1
    accum = 0
    for d in reversed(numstr):
        accum += digits[d] * order
        order *= base
    return accum

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (1+i, min_secs(raw_input()))


if __name__ == "__main__":
    main()
