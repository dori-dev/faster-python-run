def def_func(int n):
    cdef int a = 0
    cdef int i = 0
    while i < n:
        a += 1
        i += 1
    return a


cpdef int cpdef_func(int n) nogil:
    cdef int a = 0
    cdef int i = 0
    while i < n:
        a += 1
        i += 1
    return a