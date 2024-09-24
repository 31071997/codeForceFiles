#include<stdio.h>
int main()
{
    int time, n, d[100], a, b, i;
    scanf("%d", &n);
    for(i= 1 ; i<=n-1; i++)
        scanf("%d", &d[i]);
    scanf("%d %d", &a, &b);
    time = 0;
    for(i = a; i<=b-1; i++)
        time += d[i];
    printf("%d\n", time);
    return 0;
}
