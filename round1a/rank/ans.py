#!/usr/bin/env python

def find_col(N, lists):
    for i in range(1, N):
        l = lists[i]
        if l[0] in lists[0]:
            c = lists[0].index(l[0])
            cur = 1
            for j in range(1, N):
                if i != j and lists[j][c] == l[cur]:
                    cur += 1
                    if cur == N:
                        return l, lists[:i] + lists[i+1:]


def find_missing(N, lists):
    # step one sort lists by first element (then second, etc)
    lists.sort()

    # if any arent strictly incr in any col they are columns
    # (i think this might be guaranteed due to overlap)
    for i in range(1, len(lists)):
        if any([ lists[i][j] == lists[i-1][j] for j in range(N)]):
            col = lists[i]
            prows = lists[:i] + lists[i+1:]
            break
    else:
        # if no col find a list that contains N of the other lists at some index
        col, prows = find_col(N, lists)

    # now that we have at least one columns separate rows and cols
    rows = [prows.pop(0)]
    cols = [col]
    cindex = rows[0].index(col[0])
    cur = 1
    for r in prows:
        if cur < len(col) and r[cindex] == col[cur]:
            cur += 1
            rows.append(r)
        else:
            cols.append(r)

    assert(len(rows) == N)
    assert(len(cols) == N-1)

    print 'rows %s\ncols %s' %(rows, cols)

    # now we just need to find the missing col
    for i in range(N-1):
        if cols[i][0] == rows[0][i]:
            assert(cols[i] == [r[i] for r in rows])
        else:
            return [r[i] for r in rows]
    return [r[N-1] for r in rows]

def main():
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        lists = []
        for i in range(2*N-1):
            lists.append(map(int, raw_input().split()))
        print 'Case #%s: %s' % (i+1, ' '.join(map(str, find_missing(N, lists))))

if __name__ == "__main__":
    main()
