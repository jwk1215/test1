#! /usr/bin/python

import sys

seq = sys.argv[1]

def comp1(seq):
    comp = ''
    for s in seq:
        if s == "A":
            comp +="T"
        elif s == "C":
            comp +="G"
        elif s == "G":
            comp +="C"
        elif s == "T":
            comp +="A"
    return comp

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.ext()

    seq = sys.argv[1] #ATGTTATAG
    c1 = comp1(seq)
    print(c1)


