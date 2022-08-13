int cmpfunc( const void *a, const void *b) {
  return *(char*)a - *(char*)b;
}
bool isAnagram(char * s, char * t){
    qsort(s, (size_t) strlen(s), (size_t) sizeof(char), cmpfunc);
    qsort(t, (size_t) strlen(t), (size_t) sizeof(char), cmpfunc);
    int result = strcmp(t, s);
    printf("%d", result);
    if(result == 0){
        return true;
    }else{
        return false;
    }
    return false;
}