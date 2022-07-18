#include<stdio.h>
int add(int a, int b)
{
    int c;
    c=a+b;
    return c;
}
int main()
{ 
    // printf("Hello world\n");
    // int v=add(4,5);
    // printf("%d",v);
    // for(int i=0;i<=10;i++){
    //     printf("%d\n",i);
    // }
    int x=10;
    // printf("%d\n",++x); 
    // printf("%d\n",x++); 
    // printf("%d\n",x); 
    // printf("%d\n",--x); 
    // printf("%d\n",x--); 
    // printf("%d\n",x); 
    // printf("%d %d\n",x,x++); 
    printf("%d %d %d \n",--x,x--,x++,x);
    // printf("%d %d %d %d %d \n",x,x++,++x,--x,x--); 
}

