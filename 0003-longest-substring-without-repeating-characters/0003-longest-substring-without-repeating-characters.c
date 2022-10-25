int lengthOfLongestSubstring(char * s){
    int i=0;
    int max=0;
    int j;
    int check;
    
    if(strlen(s)==0){
        return 0;
    }   
    
    while(i<strlen(s)){
        j=i+1;
        int flag=0;
        while(check==1 && j-i<max){
            j++;
        }
        check=0;
        while(flag==0 && j<strlen(s)){
            char *temp=(char*)malloc(1024);
            memset(temp,0,1024);
            int f=0;
            while(f<=j-i){
                temp[f]=s[i+f];
                f++;
            }
            int a=0;
            while(flag==0 && a<strlen(temp)){
                char c=temp[a];
                int index=a+1;
                while(flag==0 && index<strlen(temp)){
		            if(c==temp[index]){
		                flag=1;
                        check=1;
		            }
                    index++;
	            }
                a++;
            }
            if(flag==0 && max<strlen(temp)){
                max=strlen(temp);
            }
            j++;
        }
        i++;
    }
   if(max==0){
       
        return 1;
    }
   return max;
}