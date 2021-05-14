#include <iostream>
using namespace std;
int main()
{
    int a, k;
    cin>>a>>k;
    cout<<(a&~(1<<k));
}
