#include <iostream>

using namespace std;

int main()
{
    int n,max,min;
    max = 0;
    min = 100;
    cin>>n;
    int marks[n];
    for(int i=0; i<n; i++){
        cin>>marks[i];
        if(marks[i]<min)
            min = marks[i];
        if(marks[i]>max)
            max = marks[i];
    }
    
    for(int i=0; i<n; i++){
        if(marks[i] == max)
            marks[i] = min;
        printf("%u ", marks[i]);;
    }
}
