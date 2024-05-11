#include <stdio.h>
int main()
{
    int walruses, chips, i;
    scanf("%d %d", &walruses, &chips);
    for(i=1; i<=walruses; i++)
    {
        if(chips >= i)
            chips -= i;
        else if(chips < i)
        {
            printf("%d", chips);
            break;
        }
        if(i == walruses)
            i = 0;
    }
    return 0;
}
