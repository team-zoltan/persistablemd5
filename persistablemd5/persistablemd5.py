# -*- coding: utf-8 -*-
"""
persistablemd5.py

class PersistableMD5

create the digest,
update it as an upload happens,
persist it to disk,
load it again, and
continue updating where we left off.
that works with MD5 in general but not with Python's hashlib md5
"""
from hashlib import md5
from md5hack import getstate, setstate


class PersistableMD5(object):
    """
    persistable md5 object
    """
    def __init__(self, data=""):
        self._md5 = md5(data)

    def __getattr__(self, name):
        return getattr(self._md5, name)

    def __getstate__(self):
        return {
            'state': getstate(self._md5),
        }

    def __setstate__(self, state):
        setstate(self._md5, state['state'])
