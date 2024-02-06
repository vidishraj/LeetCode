class Solution {
public:
    int jump(vector<int>& nums) {
       vector<int> solution(nums.size());
       int runningCounter=0;
        if(nums.size()==1){     
            return 0;
        }
       solution[nums.size()-1]= 0;
       runningCounter = 2; 
       if(nums.size()==2){
           if(nums[0]>=1){
               return 1;
           }
            return 0;
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
               int min = 8000;
               for(int j = it+1;j<=it+nums[it];j++){
                if(solution[j]>0 and solution[j]<min){
                    min=solution[j];
                }
               }
               solution[it]=min==8000?0:min+1;
            }
           runningCounter++;
       }
        
       // for(int i:solution){
       //  cout<<i;
       // }z
        // cout<<solution[solution.size()-500];
        
        return solution[0];
    }
};