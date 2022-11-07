class Solution {
public:
    string longestPalindrome(string s) {
        string ans="";
        ans+=s[0];
        if(s.length()==1){
            return s;
        }
        if(s.length()==2){
            if(s[0]==s[1]){
                return s;
            }
            string ans="";
            ans+=s[0];
            return ans ;
        }
        int n=s.length();
        vector <vector<int>> memoryTable(n, vector<int>(n));
        
        for(int i=0;i<s.length();i++){ // O(n)
            memoryTable[i][i]=1;
        }
        
        for(int i=0;i<s.length()-1;i++){ // O(n)
            if(s[i]==s[i+1]){
                memoryTable[i][i+1]=1;
            }
        }
        for(int i=s.length()-1;i>=0;i--){
            for(int j=s.length()-1;j>=0;j--){
               if(i+1<s.length()-1 and j-1>=0 and memoryTable[i+1][j-1]==1 and s[i]==s[j]){
                    memoryTable[i][j]=1;
                } 
            }
        }
        // for(int i=0;i<s.length();i++){ // O(n2)
        //     for(int j=i+1;j<s.length();j++){
        //         if(memoryTable[i+1][j-1]==1 and s[i]==s[j]){
        //             memoryTable[i][j]=1;
        //         }
        //         printf("%d ,%d, %d \n", i, j,memoryTable[i+1][j-1]);
        //     }
//         // }
        
//          for(int i=0;i<s.length();i++){
//             for(int j=0;j<s.length();j++){
//                 cout<<memoryTable[i][j];
//             }
//             cout<<"\n";
//         }
        int max=0;
        for(int i=0; i<s.length() ;i++){
            for(int j=i;j<s.length();j++){
                if(memoryTable[i][j]==1 and j-i>max){
                    ans=s.substr(i, j-i+1);
                    max=j-i;
                }
            }
        }
        return ans;
    }
};