#include<stdio.h>
int main()
{
    int s1, s2, s3, s4, count = 0;
    while(scanf("%d %d %d %d", &s1, &s2, &s3, &s4))
    {
        if(s1 == s2 || s3 == s2 || s4 = s2)
        count++;
        if(s1 == s3 || s4 = s3)
        count++;
        if(s1 == s4)
        count++;
    }
    printf("%d", count);
}

