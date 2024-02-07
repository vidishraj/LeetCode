class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> leftValues(nums.size());
        vector<int> rightValues(nums.size()); 
        vector<int> solution(nums.size()); 
        int leftMultiplicant = 1;
        int rightMultiplicant = 1;
        leftValues[0]=1;
        rightValues[nums.size()-1]=1;
        for(int i = 1;i<nums.size();i++){
            leftMultiplicant*=nums[i-1];
            leftValues[i]=(leftMultiplicant);
        }
        for(int i = nums.size()-2;i>=0;i--){
            rightMultiplicant*=nums[i+1];
            rightValues[i]=(rightMultiplicant);
        }
        for(int i = 0 ; i<nums.size();i++){
            solution[i]=leftValues[i]*rightValues[i];
        }
        return solution;
    }
};