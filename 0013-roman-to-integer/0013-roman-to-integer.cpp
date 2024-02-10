class Solution {
public:
    int romanToInt(string s) {
        int total=0;
        int i=0;
        while(i<s.size()){
            if(s[i]=='I'){
                if(i+1!=s.size() and s[i+1]=='V'){
                    total+=4;
                    i+=2;
                }
                else if(i+1!=s.size() and s[i+1]=='X'){
                    total+=9;
                    i+=2;
                }
                else{
                    total+=1;
                    i+=1;
                }
            }
            else if(s[i]=='V'){
                total+=5;
                i+=1;
            }
            else if(s[i]=='X'){
                if(i+1!=s.size() and s[i+1]=='L'){
                    total+=40;
                    i+=2;
                }
                else if(i+1!=s.size() and s[i+1]=='C'){
                    total+=90;
                    i+=2;
                }
                else{
                    total+=10;
                    i+=1;
                }
            }
            else if(s[i]=='L'){
                total+=50;
                i+=1;
            }
            else if(s[i]=='C'){
                if(i+1!=s.size() and s[i+1]=='D'){
                    total+=400;
                    i+=2;
                }
                else if(i+1!=s.size() and s[i+1]=='M'){
                    total+=900;
                    i+=2;
                }
                else{
                    total+=100;
                    i+=1;
                }
            }
            else if(s[i]=='D'){
                total+=500;
                i+=1;
            }
            else if(s[i]=='M'){
                total+=1000;
                i+=1;
            }
            
        }
        return total;
    }   
};
