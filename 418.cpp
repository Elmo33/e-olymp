#include <cstdlib>
#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{   
   double S1,S2,S3,S;
   cin>>S1>>S2>>S3;
   
   S=S1+S2+S3+2*sqrt(S1*S2)+2*sqrt(S1*S3)+2*sqrt(S3*S2);
  
   cout.setf(ios::fixed);
   cout.precision(8);
   cout<<S<<endl;
   
   return 0;
}
