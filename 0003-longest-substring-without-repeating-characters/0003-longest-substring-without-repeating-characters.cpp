class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /*
            Take the longest string and then wait till
        */
       unordered_map<char,int> charMap;//keep the letter and the index
       int start=0;
       int end=0;
        if(s.size()==0){
            return 0;
        }
       int longest=1;
       while(end<s.size() and start<s.size()){
       // cout<<end<<start<<"\n";
        if(charMap.find(s[end])==charMap.end()){
            charMap[s[end]]=end;
            end++;
        }
        else{
            // cout<<"caught"<<s[end]<<"\n";
            char duplicateChar = s[end];
            
            while(s[start]!=duplicateChar){
                // cout<<"deleting"<<s[start]<<"\n";
                charMap.erase(s[start]);
                start++;   
            }
            charMap.erase(s[start]);
            start++;
            
        }
           if(end-start>longest){
               longest=end-start;
           }
        }
        // cout<<end<<start;;
        if(end-start>longest){
            return end-start;
        }
        return longest;
    }
};

