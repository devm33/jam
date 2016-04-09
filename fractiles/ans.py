#!/usr/bin/env python

# Note: didn't end up using this answer see ans_small.py

import itertools
# Leaving this here because it was a good discovery even if unused
def generate_originals(K):
    return itertools.product([False, True], repeat=K)

def tile_step(tiles, original):
    ret = []
    gold = [True]*len(original)
    for tile in tiles:
        if tile:
            ret += gold
        else:
            ret += original
    return ret

def create_final(C, original):
    current = list(original)
    for i in range(C):
        current = tile_step(current)
    return current

def generate_finals(K, C):
    for original in generate_originals(K):
        yield create_final(C, original)

def choose_tiles(K, C, S):
    """Return the tiles necessary to flip over to determine if theres gold.

    Args:
    K: length of orginal sequence
    C: number of iterations for current sequence
    S: number of tiles that can be checked
    """
    pass


def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, choose_tiles(*map(int, raw_input().split())))

if __name__ == "__main__":
    main()
