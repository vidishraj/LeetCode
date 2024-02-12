class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        /*
            Key points to note are that we need to travel till the last index where the number is greater than or == to the target
            then we use two pointers to find the solution. 
            reducing the pointer from the right reduces the sum and increasing the right pointer increases the sum. Balance till target it found.
        */
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