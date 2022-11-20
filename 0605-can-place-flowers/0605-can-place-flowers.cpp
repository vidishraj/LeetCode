class Solution {
public:
   
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i=0;
        int start=true;
        int currentRun=0;
        while(i<flowerbed.size()){
            if(flowerbed[i]==0){
                currentRun++;
            }
            else{
                if(currentRun>=2 and start==true){
                    n-=currentRun/2;
                }
                else if(currentRun>=3){
                    currentRun%2==0?n-=currentRun/2-1:n-=currentRun/2;
                }
                start=false;
                currentRun=0;
            }
            i++;
        }
        if(start==true){
            currentRun%2==1?currentRun+=1:currentRun=currentRun;
            cout<<currentRun;
            n-=currentRun/2;
        }
        else if(currentRun>=2){
            n-=currentRun/2;
        }
        if(n<=0){
            return true;
        }
        return false;
    }
};