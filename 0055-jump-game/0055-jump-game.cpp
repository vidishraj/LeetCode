class Solution {
public:
    int canJump(vector<int>& nums) {
       vector<int> solution(nums.size());
       int runningCounter=0;
        if(nums.size()==1){     
            return true;
        }
       solution[nums.size()-1]= 0;
       runningCounter = 2; 
       if(nums.size()==2){
           if(nums[0]>=1){
               return true;
           }
            return false;
       }
       if(nums[nums.size()-2]==0){
        solution[nums.size()-2]=0;
       }
       else{
        solution[nums.size()-2]=1;
       }
       for(int it = nums.size()-3;it>=0;it--){
            if(nums[it]==0){
                solution[it]=0;
            }
            if(nums[it]>=runningCounter){
                solution[it]= 1;
            }
            else{
               int min = 50000;
               for(int j = it+1;j<=it+nums[it];j++){
                if(solution[j]>0 and solution[j]<min){
                    min=solution[j];
                }
               }
               solution[it]=min==50000?0:min+1;
            }
           runningCounter++;
       }
        
        return solution[0]>0?true:false;
    }
};