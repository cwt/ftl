# -*- coding: utf-8 -*-
import hashlib
from mmap import mmap

def digest(filename, method='sha256'):
    if method not in ('sha1', 'sha224', 'sha256', 'sha384', 'sha512'):
        raise ValueError(
            'Supported methods: sha1, sha224, sha256, sha384, sha512'
        )
    h = getattr(hashlib, method)
    f = open(filename, 'r+b')
    m = mmap(f.fileno(), 0)
    return h(m).hexdigest()
