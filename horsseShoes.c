#include <stdio.h>
int main()
{
    int s[4], k = 4, i, j, buy = 0, change[4];
    for(i = 0; i < 4; i++)
    {
        scanf("%d", &s[i]);
        change[i] = 0;
    }
    for(i = 0; i < k; i++)
    {
        for(j = k-1; j > i; j--)
        {
            if(s[i] == s[j] && change[j] != 1)
            {
                buy++;
                change[j] = 1;
            }
        }
    }
    printf("%d", buy);
    return 0;
}
