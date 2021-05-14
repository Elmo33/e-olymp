#include <iostream>

using namespace std;

int main()
{
   long long n, x, card;
   card = 0;
   cin >> n;
   card = n*(n+1)/2;
   for (long i = 1; i < n; i++){ cin >> x; card -= x; }
   cout << card;
}
