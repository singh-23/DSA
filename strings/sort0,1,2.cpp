#include <bits/stdc++.h>
using namespace std;
void sort012(int a[], int n)
    {
        int l=0;
        int m=0;
        int r=n-1;
        while(m<=r){
            if(a[m]==1){
                m++;
            }
            else if(a[m]==0){
                int temp=a[m];
                a[m]=a[l];
                a[l]=temp;
                m++,l++;
            }
            else{
                int temp=a[m];
                a[m]=a[r];
                a[r]=temp;
                r--;
            }
        }