class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.size()!=t.size()){
            return false;
        }
        unordered_map<char, char> gmap;
        unordered_map<char,char> hmap;
        for(int i=0;i<s.size();i++){
            if(gmap.find(s[i])==gmap.end()){
                gmap[s[i]]=t[i];
            }
            else{
                if(gmap[s[i]]!=t[i]){
                    return false;
                }
            }
            if(hmap.find(t[i])==hmap.end()){
                hmap[t[i]]=s[i];
            }
            else{
                if(hmap[t[i]]!=s[i]){
                    return false;
                }
            }
        }
        return true;
    }
};