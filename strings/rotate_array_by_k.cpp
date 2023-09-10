#include<bits/stdc++.h>
using namespace std;
void help(vector<int>&nums,int i,int j){
        while(i<j){
            swap(nums[i],nums[j]);
            i++;
            j--;
        }
    }
    void rotate(vector<int>& nums, int k) {
        int i=0;
        int j=nums.size()-1;
        k=k%(j+1);
        help(nums,i,j);
        help(nums,0,k-1);
        help(nums,k,j);
    }