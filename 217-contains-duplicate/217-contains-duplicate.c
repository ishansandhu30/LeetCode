bool containsDuplicate(int* nums, int numsSize){
int cmp(const void *a, const void *b)
{
    return (*(int*)a - *(int*)b);
}
qsort(nums, numsSize, sizeof(int), cmp);
    
    for(int i=1; i<numsSize; i++){
        if(nums[i]==nums[i-1]){
            return true;
        } 
        
    }
   
    return false;
}
