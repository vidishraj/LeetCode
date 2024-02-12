class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
       int firstIndex=0;
       int lastIndex = -1;
       lastIndex= numbers.size()-1;
       vector<int>solution;
        while(firstIndex<lastIndex){
            if(numbers[firstIndex]+numbers[lastIndex]==target){
                solution.push_back(firstIndex+1);
                solution.push_back(lastIndex+1);
            }
            if(numbers[firstIndex]+numbers[lastIndex]>target){
                lastIndex--;
            }
            else{
                firstIndex++;
            }
        }
        return solution;
    }
};