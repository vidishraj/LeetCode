class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int currentSum=nums[0];
        for(int i=1;i<nums.size();i++){
            currentSum+=nums[i];
            nums[i]=currentSum;
        }
        return nums;
    }
};