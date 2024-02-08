class Solution {
public:
    int numSquares(int n) {
        map<int, int> squareMap;
        for(int i=1;i<101;i++){
            squareMap[i]=i*i;
        }
        map<int, int> solutionMap;
        solutionMap[1]=1;
        solutionMap[2]=2;
        solutionMap[3]=3;
        solutionMap[4]=1;
        int currentSquare=4;
        int currentNum=2;
        for(int i=5;i<=n;i++){
            if((currentNum+1)*(currentNum+1)==i){
                solutionMap[i]=1;
                currentNum++;
                currentSquare=currentNum*currentNum;
            }
            else{
                int solution = 20000;
                for(int j=currentNum;j>sqrt(currentNum);j--){
                    // if(i==869){
                    //     cout<<j<<"\t";
                    //     cout<<(j*j)<<"\t";
                    //     cout<<i-(j*j)<<"\t";
                    //     cout<<solutionMap[i-(j*j)]<<"\t";
                    //     cout<<(j-1)*(j-1)<<"\t";
                    //     cout<<i-((j-1)*(j-1))<<"\t";
                    //     cout<<solutionMap[i-((j-1)*(j-1))]<<"\n";
                    // }
                    int minimum = min(1+solutionMap[i-(j*j)], 1+solutionMap[i-((j-1)*(j-1))]);
                    solution= min(solution, minimum);
                        
                }
                solutionMap[i]=solution;
            }
           
        }
        
        return solutionMap[n];
    }
};