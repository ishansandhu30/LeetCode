
bool isAnagram(char * s, char * t){
   int table[26] = {0};
    
    if(strlen(s) != strlen(t))
        return false;

    while(*s)
        table[*(s++) - 'a']++;
    
    while(*t)
    {
        if(--table[*(t++) - 'a'] < 0)
            return false;
    }
    
    return true;
}