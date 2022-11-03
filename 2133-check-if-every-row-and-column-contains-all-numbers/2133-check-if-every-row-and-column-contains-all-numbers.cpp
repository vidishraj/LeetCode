class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        unordered_map<int, int> gmap;
        int n=matrix.size();
        for(int i=0; i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                gmap[matrix[i][j]]++;
                if(gmap[matrix[i][j]]>1 or matrix[i][j]>n or matrix[i][j]<=0){
                    return false;
                }
            }
            gmap.clear();
        }
        for(int i=0; i<matrix.size();i++){
            int colSum=0;
            for(int j=0;j<matrix[0].size();j++){
                gmap[matrix[j][i]]++;
                if(gmap[matrix[j][i]]>1 or matrix[j][i]>n or matrix[j][i]<=0){
                    return false;
                }               
            }
            gmap.clear();
           
        }
        return true;
    }
};