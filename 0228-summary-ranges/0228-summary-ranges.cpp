
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;
        if(nums.size()==0){
            return result;
        }
        string start = to_string(nums[0]);
        for(int i=0;i<nums.size()-1;i++){
            long num1=long(nums[i+1]);
            long num2 = long(nums[i]);
            long dif= num1-num2;
            if(dif!=1){
                string end = to_string(nums[i]);
                if(stoi(start)==nums[i]){
                    result.push_back(start);
                }
                else{
                    result.push_back(start+"->"+end);
                }
                start = to_string(nums[i+1]);   
            }
        }
        if(stoi(start)==nums[nums.size()-1]){
            result.push_back(start);
        }
        else{
                string end = to_string(nums[nums.size()-1]);
                result.push_back(start+"->"+end);
        }
        return result;
    }
};