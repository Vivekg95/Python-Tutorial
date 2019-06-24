#include<stdio.h>
#include<string.h> //we have added this because we are using strlen()
int main()
{
    char p[20];
    char *s = "string";
    int length = strlen(s);
    for(int i = 0;i<length;i++)
    p[i] = s[length-i];
    printf("%s",p);

    return 0;
    

}