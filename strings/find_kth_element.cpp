#include <bits/stdc++.h>
using namespace std;
// using set function
int kthSmallest(int arr[], int l, int r, int k) {
        set<int> s1;
        for(int i=l;i<r;i++){
            s1.insert(arr[i]);
        }
        
        for(int it : s1){
            if(k==1){
             return it;   
            }
            k--;
        }
        return 0;
}
//using set function
int kthSmallest(int arr[], int l, int r, int k) {
       //using priority queue
       priority_queue<int> p1 (arr,arr+(r+1));
       int max1=r+1-k;
        while(!p1.empty()){
            if(max1==0){
                return p1.top();
            }
            max1--;
            p1.pop();
        }
       return 0;
       
    }