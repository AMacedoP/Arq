#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <time.h>
using namespace std;
typedef unsigned long long int ull;


ull hallarTri(ull n){
   return n * (n + 1) / 2;
}

ull hallarPen(ull n){
   return n * ((3 * n) - 1) / 2;
}

ull hallarHex(ull n){
   return n * ((2 * n) - 1);
}

int hallarMin(ull nums[]){
   ull a = min(nums[0], min(nums[1], nums[2]));
   int minVal = 0;

   for(int i = 0; i < 3; i++){
      if (nums[i] == a){
         minVal = i;
         break;
      }
   }

   return minVal;
}

int main(){
   ull nNums[] = {286, 165, 143};
   ull nums[] = {hallarTri(nNums[0]), hallarPen(nNums[1]), hallarHex(nNums[2])};

   clock_t t = clock();
   while (1){
      if ((nums[0] == nums[1]) and (nums[1] == nums[2])){
         cout << nums[0] << " " << nNums[0] << " " << nNums[1] << " " << nNums[2] << endl;
         break;
      }

      int m = hallarMin(nums);
      nNums[m]++;

      if (m == 0)
         nums[m] = hallarTri(nNums[m]);
      else if (m == 1)
         nums[m] = hallarPen(nNums[m]);
      else if (m == 2)
         nums[m] = hallarHex(nNums[m]);
   }
   t = clock() - t;
   printf("Se demoro %.12f ms\n", (((float)t/ CLOCKS_PER_SEC) * 1000));
}
