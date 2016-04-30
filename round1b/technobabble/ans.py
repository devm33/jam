#!/usr/bin/env python

def group_by(pairs, index):
    group = {}
    for pair in pairs:
        cur = pair[index]
        if cur in group:
            group[cur] += 1
        else:
            group[cur] = 1
    return group

def real(N, pairs):
    firsts = group_by(pairs, 0)
    seconds = group_by(pairs, 1)
    fakes = 0
    for pair in pairs:
        if firsts[pair[0]] > 1 and seconds[pair[1]] > 1:
            fakes += 1
            firsts[pair[0]] -= 1
            seconds[pair[1]] -= 1
    return fakes


def main():
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        words = [raw_input().split() for _ in range(N)]
        print 'Case #%s: %s' % ((i+1), real(N, words))


if __name__ == "__main__":
    main()
