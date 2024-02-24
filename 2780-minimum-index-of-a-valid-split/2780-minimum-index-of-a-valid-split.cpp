
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        unordered_map<int,int> countMap;   
        vector<int> leftDominant(nums.size(),-1); 
        leftDominant[0]=(nums[0]);
        countMap[nums[0]]++;        
        vector<int> rightDominant(nums.size(),-1);
        for(int i= 1 ; i< nums.size()-1;i++){
            if((countMap[nums[i]]+1)*2>i+1){
                leftDominant[i]=(nums[i]);
            }
            else{
                int previousDominant = leftDominant[i-1];
                if(previousDominant!=-1 and countMap[previousDominant]*2>i+1){
                    leftDominant[i]=(previousDominant);
                }
                else{
                    leftDominant[i]=(-1);
                }
            }
            countMap[nums[i]]++;
        }
        leftDominant[nums.size()-1]=-1;   
        countMap.clear();
        rightDominant[nums.size()-1]=nums[nums.size()-1];
        countMap[nums[nums.size()-1]]++;
        for(int i=nums.size()-2;i>0;i--){
            if((countMap[nums[i]]+1)*2>nums.size()-i){
                rightDominant[i]=nums[i];
            }
            else{
                int previousDominant = rightDominant[i+1];
                if(previousDominant!=-1 and countMap[previousDominant]*2>nums.size()-i){
                    rightDominant[i]=previousDominant;
                }
                else{
                    rightDominant[i]=-1;
                }
            }
            countMap[nums[i]]++;
        }
        for(int i=0;i<nums.size()-1;i++){
            if(leftDominant[i]==rightDominant[i+1]){
                return i;
            }
        }
        return -1;
    }
};