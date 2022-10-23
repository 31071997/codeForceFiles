#include<stdio.h>
#include<stdlib.h>
int main()
{
    int i, n, j, d, height[1000], possible;
    scanf("%d %d", &n,&d);
    possible = 0;
    for(i = 0; i < n; i++)
        scanf("%d", &height[i]);
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(i != j && abs(height[i] - height[j]) <= d)
            {
                possible++;
            }
        }
    }
    printf("%d\n", possible);
    return 0;
}
