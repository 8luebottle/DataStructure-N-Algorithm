#include<stdio.h>

long factorial(int);

// Factorial
int main()
{
    int num;
    long fact;

    printf("Enter a Positive Integer\n");
    scanf("%d", &num);

    if (num < 0)
        printf("!! Factorials aren't defined for the Negative Integer !!");
    else
    {
        fact = factorial(num);
        printf("%d! =  %ld\n", num, fact);
    }

    return 0;
}

long factorial(int n)
{
    if (n == 0)
        return 1;
    else
        return (n*factorial(n-1));
}