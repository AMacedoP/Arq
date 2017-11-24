from ta1_c import esPen, hallarHex
from time import time

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
