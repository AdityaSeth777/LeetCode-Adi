class Solution {
public:
    int countNumbersWithUniqueDigits( int n, int p = 9, int f = 9 )
{
    return n>1?p*f+countNumbersWithUniqueDigits(n<=10?n-1:10,p*f,f-1):pow(10,n);
}
};