class Solution {
public:
    bool isPalindrome(int x) {
     string temp=to_string(x);
        int i=0;
        int j=temp.size()-1;
        while(i<=j){
            if( temp[i]==temp[j]){
                i++;
                j--;
            }
            else{
                return false;
            }
        }
        return true;
    }
};