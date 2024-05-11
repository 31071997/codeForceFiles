#include <stdio.h>
int main()
{
    int n, i, a[1000], b[1000];
    int number = 0, minimum = 0;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d %d", &a[i], &b[i]);
        number = (number - a[i]) + b[i];
        if(minimum<number)
            minimum = number;
    }
    printf("%d", minimum);
    return 0;
}
