from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'square Sets',
  ext_modules = cythonize("square.pyx"),
)
