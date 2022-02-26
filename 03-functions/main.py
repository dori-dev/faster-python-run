from time import time
from code import cpdef_func, def_func

number = 10_000_000


def python_func(n):
    a = 0
    i = 0
    while i < n:
        a += 1
        i += 1
    return a


start = time()
cpdef_func(number)
end = time()
cpdef = end-start
print("cpdef", cpdef)

start = time()
def_func(number)
end = time()
def_ = end-start
print("def", def_)


start = time()
python_func(number)
python = time()
print("python", python)

print()
print("def faster", int(python/def_), "time than python")
print("cpdef faster", int(python/cpdef), "time than python")
