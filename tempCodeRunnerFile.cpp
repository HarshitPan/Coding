#include<iostream>
using namespace std;
int main()
{
    long double pow=1;
    for(int i=0;i<1000;i++)
    {
        pow=pow*5;
    }
    cout<<pow;
}