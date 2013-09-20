ftl
===

FTL File Sharing

Concept
-------

The user file is calculated for its digest using algorithm such as SHA1.
The digest is checked on server that if it already exist, the user no need
to upload the file again.

If the digest is new, then the user file is splitted to multiple blocks,
which each block is calculated for its digest too. If the digest of a block
is the same, then that block is skipped.

Storage Structure
-----------------

    +---+-----------------+      +--------------+
    | F |     Digest 1    |----->| Data Block 1 |
    | i +-----------------+      +--------------+
    | l |     Digest 2    |----->| Data Block 2 |
    | e +-----------------+      +--------------+
    |   |     Digest 3    |----->| Data Block 3 |
    | D +-----------------+      +--------------+
    | i |     Digest 4    |----->| Data Block 4 |
    | g +-----------------+      +--------------+
    | e |     ~  ~  ~     |      |    ~  ~  ~   |
    | s +-----------------+      +--------------+
    | t |     Digest N    |----->| Data Block N |
    +---+-----------------+      +--------------+

