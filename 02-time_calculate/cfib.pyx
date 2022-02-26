cpdef cfib(int n):
    if n < 0:
        return 0
    if n <= 1:
        return n
    cdef long first = 0
    cdef long second = 1
    cdef int i
    for i in range(n):
        first, second = second, first+second
    return first
