
class Solution {
    
    unordered_map<int, int> gmap;
    public:
    Solution() {
        this->gmap.clear();
    }
    
    int candy(vector<int>& ratings) {
        int start = 1;
        
        for(int i=ratings.size()-1;i>0;i--){
            if(ratings[i]<ratings[i-1]){
                start++;
            }
            else if(ratings[i]>=ratings[i-1] and start!=1){
                this->gmap[i]=start;
                start=1;
            }
        }
        int begin=1;
        bool active =false;
        if(start!=1){
            active=true;
            begin=start;
        }
        int total=start;
        for(int i= 1;i<ratings.size();i++){
            
            if(this->gmap.find(i)==this->gmap.end()){
            
                //key doesnt exist in the dictionary
                if(ratings[i-1]<ratings[i]){
                    active=false;
                    total+=begin+1;
                    begin++;
                }
                else{
                    if(active){
                        begin-1!=0?total+=begin-1:total+=1;
                        begin-1!=0?begin--:begin=1;
                    }
                    else{
                        begin=1;
                        total+=begin;
                    }
                        
                }
            }
            else{
                active=true;
                if(ratings[i-1]<ratings[i]){
                    int addition=max(begin+1,this->gmap[i]);
                    total+=addition;
                    begin=this->gmap[i];
                }
                else{
                    begin=this->gmap[i];
                    total+=begin;
                }
            }
        }
        return total;
    }
};