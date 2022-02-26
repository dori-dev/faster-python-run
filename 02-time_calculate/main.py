from time import time
from fib import fib
from cfib import cfib

number = 7000


start = time()
for i in range(-5, number):
    cfib(i)
end = time()
cython_time = end-start
print("cython", cython_time)

start = time()
for i in range(-5, number):
    fib(i)
end = time()
python_time = end-start
print("python", python_time)


print()
print("cython", int(python_time/cython_time), "time faster")
