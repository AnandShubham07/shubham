int removeDuplicates(int* nums, int numsSize) {
    int i =0;
    int l=0;
    int r=0;
  //  while(left<right)
 //   {
      for(int j=0;j<numsSize;j++)
      {   
        if(nums[j]==nums[i])
        {
          
          r++;
        }
        else{
            i++;
            nums[i]=nums[r];
            r++;
            l++;
        }
       }
  //  }
    return l+1;
}