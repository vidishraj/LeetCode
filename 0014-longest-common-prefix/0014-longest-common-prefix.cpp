class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        /*
            Take the entire first word as the longestPRefix
            at every word, check the length of the word and then -> if word length is less than currentWOrd length 
            compare the len(word) -1 index char, come down till char matches and make the longestPRefix lenght that
        */
        
        int longestPrefix =strs[0].size();
        string curr= strs[0];
        int lastIndex= curr.size()-1;
        int currentPrefix=0;
        for(int i =1;i<strs.size();i++){
            if(curr.size()>strs[i].size()){
                lastIndex = strs[i].size()-1;
            }
            int startIndex=0;
            currentPrefix=0;
            while(startIndex<=lastIndex and curr[startIndex]==strs[i][startIndex] and startIndex<longestPrefix){
                currentPrefix++;
                startIndex++;
            }
            longestPrefix=currentPrefix;
            curr=strs[i];
        }
        return strs[0].substr(0, longestPrefix);
    }
};
