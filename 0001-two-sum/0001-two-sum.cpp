class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            if(map[target-nums[i]]!=0){
                res.push_back(map[target-nums[i]]-1);
                res.push_back(i);
                return res;
            }            
            map[nums[i]]=i+1;
        }
        return res;
    }
};