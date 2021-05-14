//g++  7.4.0

#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    float x1, y1, r1, x2, y2, r2;
    float d;
    cin>>x1>>y1>>r1>>x2>>y2>>r2;
    d = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
    
    if (x1 == x2 && y1 == y2 && r1 == r2) cout << -1;
    
    else if(d == r1 + r2 || d == abs(r1 - r2)) cout<<1;
    else if(d < r1 + r2 && d > abs(r1 - r2)) cout<<2;
    
    else cout<<0;
}
