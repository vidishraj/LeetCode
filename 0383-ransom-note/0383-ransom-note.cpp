class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> countMap;
        for(char c:magazine){
            countMap[c]++;
        }
        for(char c:ransomNote){
            if(countMap.find(c)==countMap.end()){
                return false;
            }
            else{
                countMap[c]--;
                if(countMap[c]==0){
                    countMap.erase(c);
                }
            }
        }
        return true;
    }
};