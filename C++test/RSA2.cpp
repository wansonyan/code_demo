
#include<bits/stdc++.h> 
using namespace std;

long long p = 101 , q = 103;
long long n = p*q;
long long fn = (p-1)*(q-1);
long long e;
long long b1[14];//存放e的二进制 
long long size1;//e的二进制位数 
long long b2[14];//存放d的二进制 
long long size2;//d的二进制位数 

//快速指数运算，m为底；b为数组，是指数的二进制形式；size为指数的二进制形式的位数 
long long fin(long long m ,long long *b , long long size){
	long long num = 1;
	for(int i = size - 1 ; i >= 0 ; i--){
		num = (num * num)%n;
		if(b[i] == 1){
			num = (num * m)%n;
		}
	}
	return num;
}

bool check(long long n){//素性检测 
	long long h = n - 1 , g[100000] , size3 , d , i = 0 , x;
	while(h!=0){ 
		g[i] = h % 2;
		i++;
		h = h / 2;
	}
	size3 = i;
	for(int j=0; j<5; j++){
        long long a = rand() % 1000;
        d = 1;
        for(i = size3 - 1 ; i >= 0 ; i--){
        	x = d;
        	d = (d * d) % n;
        	if(d==1&&x!=1&&x!=n-1)
        		return false;
        	if(g[i]==1){
        		d = (d * a) % n;
			}
		}
		if(d!=1)
			return false;
    }
    return true;
}

long long ni(){//求乘法逆元 
	long long x1 = 1 , x2 = 0 , x3 = fn , y1 = 0 , y2 = 1 , y3 = e , t1 , t2 , t3 , Q;
	while(y3!=1){
		Q = x3/y3;
		t1 = x1-Q*y1;
		t2 = x2-Q*y2;
		t3 = x3-Q*y3;
		x1 = y1;
		x2 = y2;
		x3 = y3;
		y1 = t1;
		y2 = t2;
		y3 = t3;
		if(y3==0){
			return -1;
		}
	}
	if(y2<0){
		y2 += fn;
	}
	return y2;
}

long long encryption(long long m){//加密算法 
	long long c;
	c = fin(m,b1,size1);//指数运算 
	return c;
}

long long decryption(long long c){//解密算法 
	long long m;
	m = fin(c,b2,size2);//指数运算 
	return m;
}

int main(){
	long long m = 100;//存放明文 
	long long c;//存放密文 
	
	//对p，q进行素性检测，若并不是素数则自增再检测，直到为素数为止 
	while(check(p)!=1){
		p++;
	}
	while(check(q)!=1){
		q++;
	}
	n = q * p;
	fn = (p - 1) * (q - 1); 
	
	e = rand()%fn;
	while(1){
		if(__gcd(e,fn)==1)
			break;
		e = (e + 1) % fn;
		if(e <= 2)
			e = 3;
	} 
	
	//计算e的二进制形式以及二级制位数 
	long long h = e,i=0;
	while(h!=0){ 
		b1[i] = h%2;
		i++;
		h=h/2;
	}
	size1=i;
	
	//计算e对于φ（n）的乘法逆元d 
	long long d = ni();
	
	//计算d的二进制形式以及二级制位数 
	h = d;
	i = 0;
	while(h!=0){
		b2[i] = h%2;
		i++;
		h=h/2;
	}
	size2=i;
	
	cout<<"明文："<<m<<endl; 
	//加密 
	c = encryption(m);
	cout<<"加密后："<<c<<endl;
	
	//加密 
	long long m1 = decryption(c);
	cout<<"解密后："<<m1<<endl;
	return 0;
}
