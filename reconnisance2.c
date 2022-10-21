#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main()
{
    int n, a[100], i, min, change, index[2], temp;
    scanf("%d", &n);
    for(i = 1; i <= n; i++)
        scanf("%d", &a[i]);
    a[n+1] = a[1];
    for(i = 1; i <= n; i++)
    {
        if(i == 1)
        {
            min = abs(a[i] - a[i+1]);
            index[0] = i;
            index[1] = i+1;
        }
        else if(abs(a[i] - a[i+1])< min)
        {
            min = abs(a[i] - a[i+1]);
            index[0] = i;
            index[1] = i+1;
        }
    }
    if(index[1] == n+1)
    {
        index[1] = 1;
    }
    printf("%d %d\n", index[0], index[1]);
}
