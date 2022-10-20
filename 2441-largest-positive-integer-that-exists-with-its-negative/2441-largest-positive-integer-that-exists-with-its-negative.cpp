class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if(nums[0]>0){
            return -1;
        }
        int left=0;
        int right=nums.size()-1;
        while(left<right){
            if(abs(nums[left])<nums[right]){
                right--;
            }
            else if(abs(nums[left])>nums[right]){
                left++;
            }
            if(nums[left]==-nums[right]){
                return nums[right];
            }
        }
        return -1;
            
    }
};