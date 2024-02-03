class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int slow = 0 ;
        int count = 0 ;
        int currentElement = nums[0];
        bool duplicateFound = false;
        int currentCount= 0;
        for(int i= 0 ;i<nums.size();i++){
            if(nums[i]==currentElement){
                currentCount++;
            }
            else if(nums[i]!=currentElement){
                currentCount=1;
                currentElement=nums[i];
                duplicateFound=false;
            }
            if(currentCount>2){
                count++;
            }
            if(currentCount==3){
                duplicateFound=true;
            }
            if(!duplicateFound){
                int temp = nums[i];
                nums[i]= nums[slow];
                nums[slow] = temp;
                slow++;
            }
        }
        return nums.size()-count;
    }
};