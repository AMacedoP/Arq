#include <stdio.h>
#include <math.h>
#include <time.h>

using namespace std;
typedef long long int ll;

bool esPen(ll aux){
   double n = (sqrt(24 * aux + 1) + 1) / 6;
   if (n == (ll)n)
      return 1;
   return 0;
}

ll hallarHex(ll n){
   return n * (2 * n - 1);
}

int main(){
   ll n = 143;
   ll aux;

   clock_t t = clock();
   while (1){
      n++;
      aux = hallarHex(n);

      if (esPen(aux))
         break;
   }

   printf("%lli\n", aux);
   t = clock() - t;
   printf("Se demoro %.12f ms\n", (((float)t / CLOCKS_PER_SEC) * 1000));
}
