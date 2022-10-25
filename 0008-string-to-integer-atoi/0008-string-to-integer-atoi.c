
int myAtoi(char * s){
    int flag=0;   //0 will signify that the number is positive, if it is set to 1, that means its negative
    //this will be checked in the end
    int limit=2147483647;  //a limit to check
    long long res=0;
    int size=strlen(s);
    int i=0; //will act as an iteratoy. 
//the first rule is that we have to check for is if there are any leading white space
    if( s[i]==' '){
        while(s[i]==' '){
            i++;
        }
    }
    //now i is at where the first character 
    if(s[i]=='-'  ||s[i]=='+'){//checking whether the number is negative
        if( s[i]=='-'){
            flag=1;
        }
        i++;
    }
    if(s[i]=='0'){//to ignore any leading zeros
        while(s[i]=='0'){
            i++;
        }
    }
    //now the next character should be either a number or a letter
    //if a letter than return 0, else parse
    if( s[i]<'1' || s[i]>'9'){
        return 0;
    }
    else{
        //now we are going to measure the length from this point to the next non-digit or end of the str
        int j=i;
        while(i<size && (s[i]>=48 && s[i]<=57)){
            i++;
        }
        i--;
        int m=10;
        if(i-j>9){
            if(flag==1){
                return INT_MIN;
            }
            return INT_MAX;
        }
        m=pow(m,i-j);
        while(j<=i && s[j]){
            char c=s[j];
            long digit=(int)c-48;
            res=res+digit*m;
            m=m/10;
            j++;
        }
        
    }
    printf("%d", res);
    if( res<=INT_MIN ||res>=INT_MAX){
        if(flag==1 && res==INT_MAX){
            return INT_MIN+1;
        }
        else if(flag==1 &&res>INT_MAX){
            return INT_MIN;
        }
        else if(flag==0 && res==INT_MAX){
            return limit;
        }
        return INT_MAX;
    }
    if( flag==1){
        res=-(res);
    }
    
    
    return res;
}