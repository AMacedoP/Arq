from math import sqrt
from time import time

def esPen(aux):
   n = (sqrt(24 * aux + 1) + 1) / 6
   if (n).is_integer():
      return True
   return False

def hallarHex(n):
   return n * (2 * n -1)

def main():
   n = 143
   aux = 0
   startT = time()
   while True:
      n = n + 1;
      aux = hallarHex(n)

      if esPen(aux):
         break

   print aux, n
   endT = time()
   print "Se demoro " + str((endT - startT) * 1000) + " ms"

main()
