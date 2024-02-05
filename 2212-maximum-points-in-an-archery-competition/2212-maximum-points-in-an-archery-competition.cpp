class Solution {
    int bestPoints;
    vector<int> scoreCard;
public:

    void checkBothConditionRecursive(int index, vector<int> &arrows, int arrowsLeft, int currentPoints, vector<int> currentScoreCard){
        if(index==arrows.size()){
            if(currentPoints>this->bestPoints){
                if(arrowsLeft>0){
                    currentScoreCard[0]=arrowsLeft;
                }
                this->scoreCard=currentScoreCard;
                this->bestPoints=currentPoints;
            }
                return;
        }
        
        // cout<<index;
        // cout<<arrowsLeft;
        // cout<<"\t";
        // cout<<currentPoints;
        // cout<<'\n';
        //condition 1-> We check if we can win the points here from alice and reduce the arrows.
        //maybe check if we should win 0 points at all?
        if(index!=0 and arrows[index]+1<=arrowsLeft){
            currentScoreCard.push_back(0);
            this->checkBothConditionRecursive(index+1, arrows, arrowsLeft, currentPoints,currentScoreCard);//condition where we dont win the current points
            arrowsLeft-=arrows[index]+1;
            currentPoints+=index;
            currentScoreCard.pop_back();
            currentScoreCard.push_back(arrows[index]+1);
            this->checkBothConditionRecursive(index+1, arrows, arrowsLeft,currentPoints, currentScoreCard);//condition where we win the current points
        }
        else{
            currentScoreCard.push_back(0);
            this->checkBothConditionRecursive(index+1, arrows, arrowsLeft, currentPoints, currentScoreCard);//condition where we dont win the current points because 
            //we cant possibly win the current points or because the index is 0
        }
            
    }

    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        /* the algo should be -> write a recursive function that has two checks-> do we win this point or do we not win this point?
            We keep doing this for all cases till we run out of arrows. Hence in a way, we are checking all the possibilities.
        */
        this->scoreCard.clear();
        this->bestPoints=0;
        vector<int> emptyVector;
        this->checkBothConditionRecursive(0, aliceArrows, numArrows, 0, emptyVector);
        return this->scoreCard;
    }
};