#include<bits/stdc++.h>
using namespace std;
int maxSubArray(vector<int>& arr) {
        int ans=INT_MIN;
        int temp=0;
        for(int i=0;i<arr.size();i++){
            temp=temp+arr[i];
            ans=max(ans,temp);
            if(temp<0){
                temp=0;
            }
        }
        return ans;
    }