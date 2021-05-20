#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double a,b,h, answer;
    cin>>a>>b>>h;
    
    for(double i=a; i<=b; i+=h)
    {
        answer = 3*sin(i);
        printf("%f %f \n", i, answer);
    }
    
}
