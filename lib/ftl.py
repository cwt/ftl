# -*- coding: utf-8 -*-
import hashlib
from mmap import mmap

class Digest(object):
    def __init__(self, filename, method='sha256'):
        if method not in ('sha224', 'sha256', 'sha384', 'sha512'):
            raise ValueError(
                    'Supported methods: sha224, sha256, sha384, sha512'
            )
        self.hash_method = getattr(hashlib, method)
        self.final_hash = None
        with open(filename, 'r+b') as f:
            self.file = mmap(f.fileno(), 0)

    def ichunks(self, size=4096):
        h = self.hash_method
        self.final_hash = self.hash_method()
        while self.file.tell() < self.file.size():
            data = self.file.read(size)
            self.final_hash.update(data)
            yield (h(data).hexdigest(), data)

    def hexdigest(self, size=4096):
        if self.final_hash is None:
            all(self.ichunks(size))
        return self.final_hash.hexdigest()

