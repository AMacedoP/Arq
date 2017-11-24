from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
      Extension("ta2_c",
         sources = ["ta2_c.pyx"],
         libraries = ["m"]
      )
]

setup(
   name = "ta2_c",
   ext_modules = cythonize(ext_modules)
)
