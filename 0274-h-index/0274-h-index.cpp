class Solution {
public:
    int hIndex(vector<int>& citations) {
        /*
            We will use a map to map out the values to their occurences and then have a running counter
            for eg. [[3, 0, 6, 1, 5]]
            ->
            {
                3:1
                0:1
                6:1
                1:1
                5:1
            }
            sort this map or order this map. If we use an ordered map-> we will have complexity->o(nlongn)
            after sorting->
            {
                0:1
                1:1
                3:1
                5:1
                6:1
            }
            we iterate through this map and increase the counter in every iteration. 
            At any point where key>=counter we set h index as that value
        */
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
            // cout<<it->first;
            // cout<<it->second;
            // cout<<counter;
            // cout<<'\n';
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