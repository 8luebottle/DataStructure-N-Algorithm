#include <stdio.h>

// Linear Search
int LSearch(int ar[], int len, int target)
{
    int i;
    for(i=0; i<len; i++)
    {
        if(ar[i] == target)
	    return i;
    }
    return -1;
}


// Binary Search
int BSearch(int ar[], int len, int target)
{
    int first = 0;
    int last  = len-1;
    int mid;

    while(first <= last)
    {
        mid = (first+last)/2;
	
	if(target == ar[mid])
	{
	    return mid;
	}
	else
	{
	    if(target < ar[mid])
	        last = mid-1;
	    else
		first= mid+1;
	}
    }
    return -1; // if not found
}

