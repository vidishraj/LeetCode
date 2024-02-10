class Solution {
public:
    int strStr(string haystack, string needle) {
        for(int i=0;i<haystack.size();i++){
            if(haystack[i]==needle[0]){
                int start=0;
                while(start<needle.size() and needle[start]==haystack[start+i]){
                    start++;
                }
                if(start==needle.size()){
                    return i;
                }
            }
        }
        return -1;
    }
};