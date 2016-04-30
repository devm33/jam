#!/usr/bin/env python

def scores(sa, sb):
    # work with strings as lists
    a = list(sa)
    b = list(sb)
    # get the length
    n = len(a)
    assert n == len(b)
    # first can replace any unmatched ?'s
    for i in range(n):
        if a[i] == '?' and b[i] != '?':
            a[i] = b[i]
        elif a[i] != '?' and b[i] == '?':
            b[i] = a[i]

    # now all ?'s are matching and there are two cases
    if a[0] == '?':
        a[0] = b[0] = '0'
    va = 0
    vb = 0
    for i in range(1, n):
        if a[i] == '?':
            if a[i-1] == b[i-1]:
                a[i] = b[i] = '0'
            elif va < vb:
                a[i] = '9'
                b[i] = '0'
            else:
                a[i] = '0'
                b[i] = '9'
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
