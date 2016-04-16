#!/usr/bin/env python

def max_circle(N, bff):
    lengths = []
    unions = []
    for i in range(N):
        cur = i
        seen = set([i])
        while bff[cur] not in seen:
            addable = cur == bff[bff[cur]]
            cur = bff[cur]
            seen.add(cur)
        if addable:
            unions.append(seen)
            if bff.count(cur) > 1:
                lengths.append(len(seen)+1)
        else:
            lengths.append(len(seen))
    for s in unions:
        for i, u in enumerate(unions):
            if not u & s:
                unions[i] = u | s
    for u in unions:
        lengths.append(len(u))
    return max(lengths)

def main():
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        bff = map(lambda x: x-1, map(int, raw_input().split()))
        print 'Case #%s: %s' % (i+1, max_circle(N, bff))

if __name__ == "__main__":
    main()
