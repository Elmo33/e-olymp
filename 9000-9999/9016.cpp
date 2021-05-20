//g++  7.4.0

#include <iostream>
using namespace std;

int main()
{
    long long n, q, nums;
    cin>>n>>q;

    nums = n;
    long long a[nums], i=0;
    
    for (i=0;i<n;i++) cin>>a[i];

    while(q--)
    {
        long long x;
        cin>>x;
        int m=0, r=nums-1, k;
    
        while(m<=r){
            k = (m+r)/2;
            if(x==a[k]) { k=nums; break; }
            else if(x>a[k]) m=k+1;
            else r=k-1;
        }
    
        if(k==nums) cout<<"YES"<<"\n";
        else cout<<"NO"<<"\n";   
    }
}
