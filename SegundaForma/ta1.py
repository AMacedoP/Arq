from math import sqrt
import timeit

def esPen(aux):
   n = (sqrt(24 * aux + 1) + 1) / 6
   if (n).is_integer():
      return True
   return False

def hallarHex(n):
   return n * (2 * n -1)

def hallar():
   n = 143
   aux = 0
   while True:
      n = n + 1;
      aux = hallarHex(n)

      if esPen(aux):
         break

def main():
   times = 1000
   t = timeit.timeit('hallar()', setup = "from __main__ import hallar", number = times)
   print "Se demoro " + str((t / times) * 1000) + " ms"

main()
