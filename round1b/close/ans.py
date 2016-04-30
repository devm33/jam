#!/usr/bin/env python

def scores(sa, sb):
    # work with strings as lists
    a = list(sa)
    b = list(sb)
    # get the length
    n = len(a)
    assert n == len(b)

    # fill out question marks
    if a[0] == '?' and b[0] == '?':
        a[0] = b[0] = '0'
    elif a[0] == '?':
        a[0] = b[0]
    elif b[0] == '?':
        b[0] = a[0]
    va = int(a[0])
    vb = int(b[0])
    for i in range(1, n):
        if a[i] == '?' and b[i] == '?':
            if va == vb:
                a[i] = b[i] = '0'
            elif va < vb:
                a[i] = '9'
                b[i] = '0'
            else:
                a[i] = '0'
                b[i] = '9'
        elif a[i] == '?':
            if va < vb:
                a[i] = '9'
            elif va > vb:
                a[i] = '0'
            else:
                a[i] = b[i]
        elif b[i] == '?':
            if vb < va:
                b[i] = '9'
            elif vb > va:
                b[i] = '0'
            else:
                b[i] = a[i]

        va = 10 * va + int(a[i])
        vb = 10 * vb + int(b[i])

    # return scoreboard string
    return ''.join(a) + ' ' + ''.join(b)


def main():
    T = int(raw_input())
    for i in range(T):
        a, b = raw_input().split()
        print 'Case #%s: %s' % ((i+1), scores(a, b))


if __name__ == "__main__":
    main()
