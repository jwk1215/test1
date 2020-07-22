#! /usr/bin/env python

import sys

f = '061.fasta'

d = {}

with open(f, 'r') as handle:
    for line in handle:
        if line.startwith("@"):
            print(


