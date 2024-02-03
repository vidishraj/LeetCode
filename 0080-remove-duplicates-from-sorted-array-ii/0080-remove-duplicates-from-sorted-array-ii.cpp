class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // I want to keep two pointers and a single counter. Slow stops whenever the condition fails and then starts swapping when the fast pointer encounters another different element. 
        // Make the counter count all the duplicate elements with count more than 2. 
        int fast = 0 ;
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
                // slow = i;
                duplicateFound=true;
            }
            if(!duplicateFound){
                int temp = nums[fast];
                nums[fast]= nums[slow];
                nums[slow] = temp;
                slow++;
            }
            fast++;
        }
        // cout>>nums;
        // cout<<count;
        // for(int i= 0 ;i<nums.size();i++){
        //     cout<<nums[i];
        // }
        return nums.size()-count;
    }
};