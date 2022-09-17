#include<stdio.h>
int main()
{
    int n, m, i, j, count, a, b;
    scanf("%d %d", &n, &m);
    count = 0;
    for(i = 0 ; i <= n; i++)
    {
        for(j = 0; j <= m; j++)
        {
            if((i*i)+j == n && (j*j)+i == m)
                count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
