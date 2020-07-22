#! /usr/bin/env python


import sys


def comp2(seq):
    d_comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    comp = ''
    for s in seq:
        comp += d_comp[s]
    return comp


if __name__ == "__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()

    seq = sys.argv[1] #ATGTTATAG
    c2 = comp2(seq)
    print(c2)



