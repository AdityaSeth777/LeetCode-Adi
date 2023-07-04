/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** fizzBuzz(int n, int* returnSize){

char **res=(char**)calloc(n,sizeof(char *));int c=0;
for(int i=1;i<=n;i++)
{
    if(i%3==0&&i%5==0)
    {
        *(res+c)=(char *)calloc(9,sizeof(char));
        res[c][0]='F';res[c][1]='i';res[c][2]='z';
        res[c][3]='z';res[c][4]='B';res[c][5]='u';
        res[c][6]='z';res[c][7]='z';res[c][8]='\0';
        c++;
    }
    else if(i%3==0)
    {
        *(res+c)=(char *)calloc(5,sizeof(char));
        res[c][0]='F';res[c][1]='i';res[c][2]='z';
        res[c][3]='z';res[c][4]='\0';
        c++;
    }
    else if(i%5==0)
    {
        *(res+c)=(char *)calloc(5,sizeof(char));
        res[c][0]='B';res[c][1]='u';res[c][2]='z';
        res[c][3]='z';res[c][4]='\0';
        c++;
    }
    else
    {
        int x=0,y=i;
        while(y)
        {
            x++;
            y=y/10;
        }
        *(res+c)=(char *)calloc(x+1,sizeof(char));
        res[c][x]='\0';
        x--;
        y=i;
        while(y)
        {
            int m=y%10;
            res[c][x--]=48+m;
            y=y/10;
        }
        c++;
    }
    
}
*returnSize=c;
return res;
}