#include<stdio.h>
int main()
{
    long long n;
    int lucky;
    scanf("%lld", &n);
    lucky = 0;
    while(n > 0)
    {
        if(n%10 == 4 || n%10 == 7)
            lucky++;
        n/=10;
    }
    if(lucky == 4 || lucky == 7)
        printf("YES\n");
    else
        printf("NO\n");
    return 0;
}
