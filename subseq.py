#!/bin/python

'''
function:
    extract sequence from FASTQ files by the ID
usage:
    python subseq.py id fn
    
    two input arguments:
        id: sequence ID starting with @
        fn: file name (a fastq file)
'''

import sys

def subseq(id, fn):
    with open(fn) as fp:
        for i, line in enumerate(fp):
            if i % 4 == 0:
                if line.strip().startswith(id):
                    return next(fp)

if __name__ == "__main__":
    id = sys.argv[1]
    fn = sys.argv[2]
    
    print subseq(id, fn)
