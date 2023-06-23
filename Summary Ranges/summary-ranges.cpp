class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        int n= nums.size();
    
        vector<string>res;
        if(n==0) return res;
        vector<vector<int>>ans;
        vector<int>temp;
        temp.push_back(nums[0]);
        for(int i=1; i<n; i++){
            if(nums[i]==nums[i-1]+1){
                temp.push_back(nums[i]);
            }
            else{
                ans.push_back(temp);
                temp.clear();
                temp.push_back(nums[i]);
            }
        }
        ans.push_back(temp);
        for(auto x: ans){
            int siz= x.size();
            for(int i=0; i<siz; i++){
                cout<<x[i]<<" ";
            }
            cout<<endl;
        }
        for(int i=0; i<ans.size(); i++){
            int k= ans[i].size();
            int mini= ans[i][0];
            int maxi= ans[i][k-1];
            if(ans[i].size()==1){
                res.push_back(to_string(mini));
                
            }
            else{
            string temp="";
            temp+= to_string(mini);
            temp+="->";
            temp+= to_string(maxi);
            res.push_back(temp);
            }
        }
        return res;
        
    }
};