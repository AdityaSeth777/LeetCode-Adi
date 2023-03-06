class Solution {
public:
    int findKthPositive(vector<int>& arr, int sum) {
        //we are pushing back into the arr 
        arr.push_back(1000000);
        
        int n=arr.size();
        //we have created a prev variable for having count
        int prev=0;
        //storing the ans
        int ans=0;
        //we are running the for loop till the end of arr 
        
        for(int i=0;i<n;i++){
            //we are calculating the difference between two values prev and arr[i]
            //and updating prev to arr[i] at the end.
            int val=arr[i]-prev-1;
            //if the val less than the sum then we dont have our kth element in this interval
            if(val<sum){
                sum-=val;
            }
            //if the val less or equal then we will have our ans as prev + sum
            else{
                ans=prev+sum;
                break;
            }
            //updating prev to arr[i]
            prev=arr[i];
        }
        //poping the value we inserted
        arr.pop_back();
        return ans;
    }
};