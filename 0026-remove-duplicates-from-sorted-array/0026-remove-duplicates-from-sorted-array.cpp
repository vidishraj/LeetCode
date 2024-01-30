class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //same as the previous 2 pointer question except our val is changing
        set<int> newSet = {};
        for(int it = 0;it<nums.size();it++){
            newSet.insert(nums.at(it));
        }
        nums.clear();
        for (auto it = newSet.begin(); it != newSet.end(); ++it) {
            nums.push_back(*it);
        }
        return nums.size();
    }
};