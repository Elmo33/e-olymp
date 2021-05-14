#include <iostream>
using namespace std;
 
int main()
{
    unsigned long long int n, a, answer;
    cin >> n >> a;
    if (a > 1)
    {
        answer = n*a;
        for(unsigned long long int i = n-1; i > 0; --i)
            answer = (answer+i)*a;
    }
    else
        answer = n*(n+1)/2;
    cout << answer;
    return 0;
}
