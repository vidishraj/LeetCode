class Solution {
public:
    string convert(string s, int numRows) {
        string ans ="";
        int start=0;
        if(s.size()==1){
            return s;
        }
        int line=1;
        int upwardClimb=-1;
        int downwardClimb=-1;
        while(ans.size()<s.size()){
            downwardClimb=2*(numRows-line);
            upwardClimb=2*(line-1);
            if(downwardClimb==0){
                downwardClimb=upwardClimb;
            }
            if(upwardClimb==0){
                upwardClimb=downwardClimb;
            }
            if(downwardClimb==0){
                return s;
            }
            bool direction=true;
            int localStart = start;
            cout<<downwardClimb<<upwardClimb<<ans<<"\t";
            while(localStart<s.size()){
                ans.push_back(s[localStart]);
                if(direction){
                 localStart+=downwardClimb;   
                    direction=false;
                }
                else{
                    localStart+=upwardClimb;
                    direction=true;
                }
            }
            start++;
            line++;
        }
        return ans;
    }
};