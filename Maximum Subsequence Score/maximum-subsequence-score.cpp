class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<vector<int>> nums;
        int n = nums1.size();
        for(int i=0; i<n; ++i){
            nums.push_back({nums2[i],nums1[i]});
        }
        sort(begin(nums),end(nums));
        vector<long long> maxk(n,0ll);
        long long ans = 0, sum = nums[n-1][1];
        multiset<int> st;
        st.insert(nums[n-1][1]);
        maxk[n-1] = nums[n-1][1];
        for(int i=n-2; i>=0; --i){
            int curr = nums[i][1];
            if(st.size() < k-1){
                st.insert(curr);
                sum += curr;
            }
            else{
                if(*st.begin()<=curr){
                    sum += curr;
                    sum -= *st.begin();
                    st.erase(st.begin());
                    st.insert(curr);
                }
            }
            maxk[i] = sum;
        }
        maxk.push_back(0);
        for(int i=0; i<=n-k; ++i){
            if(k == 1)
                ans = max(ans,((long long)nums[i][1] * nums[i][0]));
            else
            ans = max(ans,(maxk[i+1]+nums[i][1])*nums[i][0]);
        }
        return ans;
    }
};