from libc.math cimport sqrt

def esPen(long int aux):
   cdef double n = (sqrt(24 * aux + 1) + 1) / 6
   if (n).is_integer():
      return True
   return False

def hallarHex(long int n):
   return n * (2 * n -1)
