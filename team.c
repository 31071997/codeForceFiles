#include<stdio.h>
int main()
{
    int n, p, v, t, a, i;
    scanf("%d", &n);
    a = 0;
    for(i=0; i< n; i++)
    {
        scanf("%d %d %d",&p, &v, &t);
        if(p+v+t >= 2)
        a++;
    }
    printf("%d\n", a);
    return 0;
}
