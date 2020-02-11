// Recursion
#include<stdio.h>

// Factorial
long factorial(int n)
{
    if (n == 0)
        return 1;
    else
        return (n*factorial(n-1));
}

// Binary Search
int BinarySearch(int ar[], int first, int last, int target)
{
    int mid;
    if(first > last)
        return -1;
    mid = (first + last) / 2;

    if(ar[mid] == target)
        return mid;
    else if(target < ar[mid])
        return BinarySearch(ar, first, mid-1, target);
    else
        return BinarySearch(ar, mid+1, last, target); 
}

int main()
{
    // Test Factorial
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

