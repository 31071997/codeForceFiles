#include<stdio.h>
int main()
{
    int n, k, place, i, a[50];
    scanf("%d %d", &n, &k);
    place = 0;
    for(i = 1; i <= n; i++)
        scanf("%d", &a[i]);
    for(i = 1; i <= n; i++)
    {
        if(i <= k && a[i] > 0)
        {
            place++;
        }
        else if(i > k && a[i] == a[k])
        {
            place++;
        }
        else
            break;
    }
    printf("%d\n", place);
    return 0;
}
