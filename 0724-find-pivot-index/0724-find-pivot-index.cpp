class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int totalSum=0;
        int result=-1;
        for(int num:nums){
            totalSum+=num;
        }
        int rightSum=0;
        for(int i=nums.size()-1;i>-1;i--){
            totalSum-=nums[i];
            if(totalSum==rightSum){
                result=i;
            }
            rightSum+=nums[i];
        }
        return result;
    }
};