#!/usr/bin/env python


def flip_to(i, arr):
    return [not v for v in reversed(arr[:i])] + arr[i:]

def children(arr):
    return [flip_to(i, arr) for i in range(1, len(arr))]

def numflips(arr):
    if all(arr):
        return 0
    q = [(arr, 0)]
    while q:
        cur, depth = q.pop()
        nxt = children(cur)
        for c in nxt:
            if all(c):
                return depth+1
            if not any(c):
                return depth+2
        q += [(c, depth+1) for c in nxt]

def readstack(stackstr):
    return [p == '+' for p in stackstr]

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, numflips(readstack(raw_input())))

if __name__ == "__main__":
    main()
