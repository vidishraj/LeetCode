class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        string divisor = "";
        int currentIndex = 0;
        while( divisor.size()<str1.size()){
            divisor+=str1[currentIndex];
            currentIndex+=1;
            if(str1.size() % divisor.size()==0){
                string tempDivisor = divisor;
                while(tempDivisor.size()<str1.size()){
                    tempDivisor+=divisor;
                }
                if(tempDivisor==str1){
                    break;
                }
            }
        }
        string str2Check = divisor;
        while(str2Check.size()<str2.size()){
            str2Check+=divisor;
        }
        if( str2Check!=str2){
            return "";
        }
        string maximumStr = str1.size()>str2.size()?str1:str2;
        string tempDivisor = divisor;
        string curr = divisor;
        while(tempDivisor.size()<=maximumStr.size()){ 
            if(str1.size()%tempDivisor.size()==0 && str2.size()%tempDivisor.size()==0){
                curr = tempDivisor;
            }
           tempDivisor+=divisor; 
        }
        return curr;
    }
};