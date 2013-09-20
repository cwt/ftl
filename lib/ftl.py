# -*- coding: utf-8 -*-
import hashlib
from mmap import mmap

def digest(filename, method='sha256'):
    if method not in ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'):
        raise ValueError(
            'Supported methods: md5, sha1, sha224, sha256, sha384, sha512'
        )
    h = getattr(hashlib, method)
    with open(filename, 'r+b') as f:
        m = mmap(f.fileno(), 0)
        return h(m).hexdigest()
