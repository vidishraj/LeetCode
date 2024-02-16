class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int top=0;
        int left=0;
        int bottom= matrix.size()-1;
        int right = matrix[0].size()-1;
        int centerRow = matrix.size()/2;
        int centerColumn = matrix[0].size()/2;
        int i=0;
        int j = 0;
        vector<int> result;
        if( centerRow==0 and centerColumn==0){
            result.push_back(matrix[0][0]);
            return result;
        }
        while(true){
            i = top;
            j=left;
            while(j<=right){
                result.push_back(matrix[i][j]);
                if(result.size()==matrix.size()*matrix[0].size()) return result;
                j++;
            }
            top+=1;
            i=top;
            j=right;
            while(i<=bottom){
                result.push_back(matrix[i][j]);
                if(result.size()==matrix.size()*matrix[0].size()) return result;
                i++;
            }
            right-=1;
            i=bottom;
            j=right;
            while(j>=left){
                result.push_back(matrix[i][j]);
                if(result.size()==matrix.size()*matrix[0].size()) return result;
                j--;
            }
            bottom--;
            i=bottom;
            j=left;
            while(i>=top){
                result.push_back(matrix[i][j]);
                if(result.size()==matrix.size()*matrix[0].size()) return result;
                i-=1;
            }
            left++;
        }
        
      return result;
    }
};