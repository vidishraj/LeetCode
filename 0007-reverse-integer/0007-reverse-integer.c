

int reverse(int x){
    long val=0;
    int mod;
    int flag=0;
    if(x>=INT_MAX){
        return 0;
    }
    if(x<=INT_MIN){
        return 0;
    }
    if(x<0){
        x=-1*x;
        flag=1;
    }
    while(x>0){
        mod=x%10;
        if(val*10+mod>=INT_MAX){
            return 0;
        }
        val=10*val+mod;
        x=x/10;
    }
    if(flag==1){
        val=-1*val;
    }
    //val=10*val+mod;
    return val;
}