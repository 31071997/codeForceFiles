#include<stdio.h>
#include<math.h>
int n, i;
int main()
{
    int a[1000], j, amazing, max, min;
    scanf("%d", &n);
    amazing = 0;
    for(i = 0; i< n; i++)
    {
        scanf("%d", &a[i]);
    }
    for(i = 1; i < n; i++)
    {
        max = 0;
        min = 0;
        for(j = 0; j < i; j++)
        {
            if(a[i] > a[j])
                max++;
            if(a[i] < a[j])
                min++;
        }
        if(max == j || min == j)
            amazing++;
    }
    printf("%d\n", amazing);
    return 0;
}
