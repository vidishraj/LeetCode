class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
       int firstIndex=0;
       int lastIndex = -1;
       lastIndex= numbers.size()-1;
       vector<int>solution(2);
        while(firstIndex<lastIndex){
            if(numbers[firstIndex]+numbers[lastIndex]==target){
                solution[0]=(firstIndex+1);
                solution[1]=(lastIndex+1);
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