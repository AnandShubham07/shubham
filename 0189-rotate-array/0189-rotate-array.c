void rotate(int* nums, int numsSize, int k) {
    int i=0;
    int *arr=malloc(numsSize* sizeof(int));
    k=k%numsSize;
    for(int i=0;i<numsSize;i++)
    {
        arr[i]=nums[(i+(numsSize-k))%numsSize];

    }
    for(i=0;i<numsSize;i++)
    {
        nums[i]=arr[i];
    }
}