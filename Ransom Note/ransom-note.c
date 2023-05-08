bool canConstruct(char * ransomNote, char * magazine){

int t[26] = {0};

for(char *str = magazine; *str; str++ ) {
    if(*str >= 97 && *str <= 122) {
        t[*str - 97] += 1;
    }
}

for(char *str = ransomNote; *str; str++) {
    if(t[*str -97] == 0)
        return false;
    else if (t[*str -97] > 0)
        t[*str -97] -= 1;
}

return true;
}