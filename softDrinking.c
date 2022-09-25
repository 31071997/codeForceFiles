#include<stdio.h>
int main()
{
    int n, k, l, c, d, p, nl, np, toast, slice, drink, salt;
    scanf("%d %d %d %d %d %d %d %d",&n, &k, &l, &c, &d, &p, &nl, &np);
    slice = c*d;
    if(slice < n)
        toast = 0;
    else
    {
        drink = (k*l)/(n*nl);
        salt = p/(n*np);
        if(drink < salt)
            toast = drink;
        else
            toast = salt;
    }
    if(toast > (slice/=n))
        toast = slice;
    printf("%d", toast);
    return 0;
}
