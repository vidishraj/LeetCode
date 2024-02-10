class Solution {
public:
    string intToRoman(int num) {
        /*
            Take the number and find the number it is greater than, move till there
            I             1
            V             5
            X             10
            L             50
            C             100
            D             500
            M             1000

        */
       string roman="";
       while(num!=0){
            if(num>=1000){
                roman.push_back('M');
                num=num-1000;
            }
            else if(num>=900){
                roman.push_back('C');
                roman.push_back('M');
                num=num-900;
            }
            else if(num>=500){
                roman.push_back('D');
                num=num-500;
            }
            else if(num>=400){
                roman.push_back('C');
                roman.push_back('D');
                num=num-400;
            }
            else if(num>=100){
                roman.push_back('C');
                num=num-100;
            }
            else if(num>=90){
                roman.push_back('X');
                roman.push_back('C');
                num=num-90;
            }
            else if(num>=50){
                roman.push_back('L');
                num=num-50;
            }
            else if(num>=40){
                roman.push_back('X');
                roman.push_back('L');
                num=num-40;
            }
            else if(num>=10){
                roman.push_back('X');
                num=num-10;
            }
            else if(num>=9){
                roman.push_back('I');
                roman.push_back('X');
                num=num-9;
            }
            else if(num>=5){
                roman.push_back('V');
                num=num-5;
            }
            else if(num>=4){
                roman.push_back('I');
                roman.push_back('V');
                num=num-4;
            }
            else if(num>=1){
                roman.push_back('I');
                num=num-1;
            }
       }
        return roman;
    }
};
