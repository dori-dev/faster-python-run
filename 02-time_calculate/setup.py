from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("cfib.pyx")
)

# run in terminal
# python setup.py build_ext --inplace
