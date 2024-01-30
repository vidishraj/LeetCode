class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0 ;
        if(nums.size()==0){
            return 0;
        }
        sort(nums.begin(), nums.end());
        if(nums[nums.size()-1]==val){
            int lastElement = nums.size()-1;
            while(lastElement!=-1 and nums[lastElement]==val){
                lastElement--;
            }
            if(lastElement == -1){
                return 0;
            }
            return lastElement+1;
        }
        int numsSize = nums.size();
        int startPlace = -1;
        int lastPlace = -1;
        for(int i= 0 ;i<nums.size();i++){
            // cout<<nums[i]<<"\n";
            if(nums[i]==val and startPlace == -1){
                // cout<<"HEllo"<<i;
                startPlace = i; 
            }
            if(nums[i]!=val and startPlace!=-1 and lastPlace==-1){
                // cout<<"YOOHO"<<nums[i]<<i;
                lastPlace = i-1;
            }
        }
        if(lastPlace ==-1 and startPlace==-1){
            return nums.size();
        }
        if(lastPlace == -1){
            return startPlace+1;
        }
        // cout<<startPlace<<lastPlace;
        int swapCount = 0; 
        for(int i =lastPlace+1;i<numsSize;i++){
            nums[startPlace+swapCount] = nums[i];
            nums[i]=val;
            swapCount++;
        }
        return startPlace+swapCount; 
    }
};