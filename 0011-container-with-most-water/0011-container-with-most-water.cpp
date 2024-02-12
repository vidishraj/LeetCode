class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0;
        int j=height.size()-1;
        int maxQuant= 0;
        while(i<j){
            maxQuant = max((j-i)*min(height[i], height[j]),maxQuant);
            if(height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
                
        }
        return maxQuant;
    }
};