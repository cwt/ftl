# -*- coding: utf-8 -*-

from lib.digest import FileDigest

import sys

def print_help():
    print('Usage: ftl.py [store] filename')
    exit()

if len(sys.argv) >= 3:
    command = sys.argv[1]
else:
    print_help()

chunks = {}

if command == 'store':
    i = 0
    d = 0
    for filename in sys.argv[2:]:
        fd = FileDigest(filename)
        for digest, data in fd.chunks():
            if hash in chunks:
                chunks[digest] += 1
            else:
                chunks[digest] = 1
            i += 1
        d += fd.file.size()
else:
    print_help()

print('Number of all chunks:', i)
print('Number of unique chunks:', len(chunks))
print('Delta chunks:', i - len(chunks))
print('Chunks Ratio: %.2f%%' % (100.0 * (i - len(chunks)) / i))
print('Data size:', d)
d_size = len(chunks.popitem()[0]) * len(chunks)
print('Unique digest size:', d_size)
print('Digest/Data Ratio: %.2f%%' % (100.0 * d_size / d))
