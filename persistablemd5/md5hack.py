from ctypes import *

PyObject_HEAD = [
    ('ob_refcnt', c_size_t),
    ('ob_type', c_void_p),
]

class EVP_MD(Structure):
    _fields_ = [
        ('type', c_int),
        ('pkey_type', c_int),
        ('md_size', c_int),
        ('flags', c_ulong),
        ('init', c_void_p),
        ('update', c_void_p),
        ('final', c_void_p),
        ('copy', c_void_p),
        ('cleanup', c_void_p),
        ('sign', c_void_p),
        ('verify', c_void_p),
        ('required_pkey_type', c_int*5),
        ('block_size', c_int),
        ('ctx_size', c_int),
    ]

class EVP_MD_CTX(Structure):
    _fields_ = [
        ('digest', POINTER(EVP_MD)),
        ('engine', c_void_p),
        ('flags', c_ulong),
        ('md_data', POINTER(c_char)),
    ]

class EVPobject(Structure):
    _fields_ = PyObject_HEAD + [
        ('name', py_object),
        ('ctx', EVP_MD_CTX),
    ]


def getstate(md5):
    c_evp_obj = cast(c_void_p(id(md5)), POINTER(EVPobject)).contents
    ctx = c_evp_obj.ctx
    digest = ctx.digest.contents
    return ctx.md_data[:digest.ctx_size]


def setstate(md5, state):
    c_evp_obj = cast(c_void_p(id(md5)), POINTER(EVPobject)).contents
    ctx = c_evp_obj.ctx
    digest = ctx.digest.contents
    memmove(ctx.md_data, state, digest.ctx_size)
