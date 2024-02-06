class Solution {
public:
    int hIndex(vector<int>& citations) {
        map<int, int> citationMap;
        for(int i=0;i<citations.size();i++){
            if(citationMap.find(citations[i])==citationMap.end()){
                citationMap[citations[i]] = 1;
            }
            else{
                citationMap[citations[i]]++;
            }
        }
        if(citations.size()==1){
            if(citations[0]==0){
                return 0;
            }
            return 1;
        }
        int hIndex=0;
        int counter = 0;
        int minimumCitations = 0;
        for(auto it=citationMap.rbegin();it!=citationMap.rend();it++){
            counter+=it->second;
            if(it->first<=counter and hIndex<it->first){
                hIndex=it->first;
            }
            if(counter<it->first and hIndex<counter){
                hIndex= counter;
            }
        }
        return hIndex;
    }
};