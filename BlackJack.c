#include<stdio.h>
int main()
{
    int n, result, i;
    const int queen = 10;
    scanf("%d", &n);
    result = 0;
    for(i = 1; i<= 11; i++)
    {
        if(i+queen == n)
        {
            if(i != 10)
                result += 4;
            else if(i == 10)
                result += 15;
            break;
        }
    }
    printf("%d\n", result);
    return 0;
}
