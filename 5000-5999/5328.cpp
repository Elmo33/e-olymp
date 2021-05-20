#include <iostream>

using namespace std;
int main() {
    int x, min, num;

    cin >> x;
    cin >> min;
    for(int n=1; n<x; n++){
        cin >> num;
        if(num<min) min=num;
    }
    cout << min;
}
