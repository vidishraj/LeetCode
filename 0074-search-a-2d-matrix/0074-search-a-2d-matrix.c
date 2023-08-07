bool binary_search(int* temp, int length, int target){
    int start=0;
    int mid;
    int end=length-1;
    while(start<=end){
        mid=(start+end)/2;
        if(temp[mid]==target){
            return 1;
        }
        if(temp[mid]<target){
            start=mid+1;
        }
        if( temp[mid]>target){
            end=end-1;
        }
    }
    return false;
}
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
//this is nothing but interior binary search 
    for(int i=0;i<matrixSize;i++){
        int *temp=(matrix[i]);
        printf("%d\n", temp[0]);
        if(temp[*(matrixColSize)-1]>=target){
            if(binary_search(temp, *(matrixColSize), target)){
            return true;
            }
        }
    }
    return false;
}