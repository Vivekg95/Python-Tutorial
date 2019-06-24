#include<stdio.h>
int main()
{
    int array[100],n,position,value;
    printf("\n enter the number of elements:");
    scanf("%d",&n); //value is stored
    printf("Enter the elememts \n",n);
    for(int i=0;i<n;i++)
    scanf("%d",&array[i]);
    printf("\n enter the location where you want to insert");
    scanf("%d",&position);
    printf("\n enter the value to insert");
    scanf("%d",&value);
    for(int i=n-1;i>=position-1;i--)//creating space by shifting element down
    array[i+1]=array[i];
    array[position-1]=value;// inserting element at desired space
    printf("resultant array is \n");
    for(int i=0;i<=n;i++)
    printf("%d\n",array[i]);





    /* code */
    return 0;
}
