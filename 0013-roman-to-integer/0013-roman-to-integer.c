int romanToInt(char * s){
    int i=strlen(s)-1;
    int total=0;
    while(i>=0){
        char c=s[i]; //we'll read from the back
        if(c=='I'){
            total+=1;
            i--;
        }
       else if(c=='V'){
           total+=5;
           if(i-1>=0 && s[i-1]=='I'){
                total=total-1;
                 i--;
            }
           i--;
        }
       else if(c=='X'){
            total+=10;
            if(i-1>=0 && s[i-1]=='I'){
                total=total-1;
                      i--;
            }  
           i--;
        }
       else if(c=='L'){
            total+=50;
           
            if(i-1>=0 && s[i-1]=='X'){
                total=total-10;
                i--;
            } i--;
        }
       else if(c=='C'){
            total+=100;
           
            if(i-1>=0 && s[i-1]=='X'){
                total=total-10;
                i--;
            }i--;
        }
       else if(c=='D'){
            total+=500;
            
            if(i-1>=0 && s[i-1]=='C'){
                total=total-100;
                i--;
            }i--;
           
        }
       else if(c=='M'){
            total+=1000; 
            if(i-1>=0 && s[i-1]=='C'){
                total=total-100;
                i--;
            } 
           i--;
        }
    }
    return total;
}