/*
 * @Descripttion: 
 * @version: 
 * @Author: Ryan
 * @Date: 2023-11-06 14:50:14
 * @LastEditors: Ryan
 * @LastEditTime: 2023-11-06 14:50:26
 */
#include<stdio.h>
int exgcd(int a,int b,int &x,int &y){//返回的是最大公约数.
//此时 a,b代表的是上一个式子的除数和余数
    if(b==0){//余数为0
        x=1;
        y=0;
        return a;
    }
    int r=exgcd(b,a%b,y,x);//递归求解gcd(a,b);
    y=y-a/b*x;
    return r; 
}
int main(){
    int x,y,a=6731,b=2809;
    int gcd=exgcd(a,b,x,y);
    printf("%d = (%d)*%d + (%d)*%d",gcd,x,a,y,b);
}