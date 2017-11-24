from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules=[
      Extension("ta1_c",
         sources = ["ta1_c.pyx"],
         libraries = ["m"]
      )
]

setup(
   name = "ta1_c",
   ext_modules = cythonize(ext_modules)
)
