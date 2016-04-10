#!/usr/bin/env python

NO = 'IMPOSSIBLE'

def choose_tiles(K, C, S):
    # special case for single tile
    if K == 1:
        return '1' if S > 0 else NO
    # special case for single level have to check first K
    if C == 1:
        return NO if S < K else str_arr(range(1, K+1))
    # otherwise with C > 1 have to check all of the first K except the 1st
    return NO if S < K - 1 else str_arr(range(2, K+1))

def str_arr(arr):
    return ' '.join(map(str, arr))

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, choose_tiles(*map(int, raw_input().split())))

if __name__ == "__main__":
    main()
