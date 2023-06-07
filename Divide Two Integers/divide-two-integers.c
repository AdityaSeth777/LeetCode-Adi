int divide( int dividend, int divisor )
{
    long int cnt, ans = 0 ;
    long int x = dividend, y = divisor ;
    bool flag = 0 ;

    if( x == INT_MIN && y == -1 ) return INT_MAX ;
    if( x == INT_MIN && y == 1 )  return INT_MIN ;

    if( x < 0 )
    {
        x *= -1 ;
        flag = 1 ;
    }

    if( y < 0  )
    {
        if( flag == 1 )
        {
            flag = 0 ;
        }

        else
        {
            flag = 1 ;
        }
        y *= -1 ;
    }

    while( x >= y )
    {
        int tmp = 0 ;
        while( x >= ( y << tmp ) )
        {
            tmp++ ;
        }
        x -= ( y << tmp-1 ) ;
        ans += 1<<tmp-1 ;
    }
    
    if( flag == 1 )
    {
        ans *= -1 ;
    }

    if( ans < INT_MIN ) return INT_MIN ;
    else if( ans > INT_MAX ) return INT_MAX ;
    else return ans ;
}