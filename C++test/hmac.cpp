#include<iostream>
#include<vector>
#include<bitset>
#include<algorithm>
using namespace std; 

typedef bitset<32> word;

vector<bool> m,k,IV,M1,M2;//m为明文，k为密钥，IV为初始向量,Mi为第i次压缩后的结果 
int compress_num=0;//表示当前是第几次压缩 
bool ipad[8]={0,0,1,1,0,1,1,0},opad[8]={0,1,0,1,1,0,1,0};
vector<bool> si,so;
word kt[4]={0x5A827999,0x6ED9EBA1,0x8F1BBCDC,0xCA62C1D6};//加法常量 

word add(word a,word b){
	word c;
	bool h=0,g,f;
	for(int l=0;l<32;l++){
		g=a[l];
		f=b[l];
		c[l]=g^f^h;
		if((g==1&&f==1)||(g==1&&h==1)||(h==1&&f==1)){
			h=1;
		}else{
			h=0;
		}
	}
	return c;
}

void Hash(vector<bool>& m){
	bool m1[512],m2[160];
	word A,B,C,D,E,a,b,c,d,e;
	word w[80],f,E1,A1,q;
	//将初始向量分成A、B、C、D、E五块 
	for(int i=0,j=31;i<160;i++){
		if(i<32*1){
			A[j]=IV[i];
			j--;
			if(j==-1)
				j=31;
		}else if(i<32*2){
			B[j]=IV[i];
			j--;
			if(j==-1)
				j=31;
		}else if(i<32*3){
			C[j]=IV[i];
			j--;
			if(j==-1)
				j=31;
		}else if(i<32*4){
			D[j]=IV[i];
			j--;
			if(j==-1)
				j=31;
		}else{
			E[j]=IV[i];
			j--;
			if(j==-1)
				j=31;
		}
	}
	//取512字节的分块 
	for(int i=0,j=0;i<m.size();i++){
		m1[j]=m[i];
		w[j/32][31-j%32]=m1[j];//生成另一个加法常量的前十六个 
		j++;
		if(j==512){//分块完成 
			j=0;
			//生成另一个加法常量的后六十四个
			for(int l=16;l<80;l++){
				q=w[l-16]^w[l-14]^w[l-8]^w[l-3]; 
				for(int v=0;v<32;v++){//向左循环移位1位 
					w[l][(v+1)%32]=q[v];
				}
			}
			//保存80轮运算之前的内容 
			a=A;
			b=B;
			c=C;
			d=D;
			e=E;
			//80轮运算 
			for(int t=0;t<80;t++){
				//计算f函数 
				if(t<20){
					f=(B&C)|(~B&D);
				}else if(40<=t<60){
					f=(B&C)|(B&D)|(C&D);
				}else{
					f=B^C^D;
				}
				//f函数加上E块，结果为E1 
				E1=add(E,f);
				//A循环左移5位得到A1 
				for(int l=0;l<32;l++){
					A1[(l+5)%32]=A[l];
				}
				//E1加A1,结果为E1 
				E1=add(E1,A1);
				//E1加两个加法常量w和kt 
				E1=add(E1,w[t]);
				E1=add(E1,kt[t/20]);
				//换位 
				E=D;
				D=C;
				for(int l=0;l<32;l++){
					C[(l+30)%32]=B[l];
				}
				B=A;
				A=E1;
			}
			//ABCDE加上80轮函数前的ABCDE
			A=add(A,a);
			B=add(B,b);
			C=add(C,c);
			D=add(D,d);
			E=add(E,e);
		}
	}
	
	int i,j;
	//将ABCDE五块放到一起 
	for(i=0,j=31;i<160;i++){
		if(i<32){
			m2[i]=A[j];
		}else if(i<32*2){
			m2[i]=B[j];
		}else if(i<32*3){
			m2[i]=C[j];
		}else if(i<32*4){
			m2[i]=D[j];
		}else{
			m2[i]=E[j];
		}
		j--;
		if(j==-1){
			j=31;
		}
	}
	if(compress_num==1){
		for(i=0;i<160;i++){
			M1.push_back(m2[i]);
		}
	}else{
		for(i=0;i<160;i++){
			M2.push_back(m2[i]);
		}
	}
}


int main(){
	//输入信息m直接在代码里赋值，16个0和16个1交替出现 
    for(int i=0;i<320;i++){
    	if(i%32<16){
    		m.push_back(0);
		}else{
			m.push_back(1);
		}
	}
	//填充明文至长度取余512等于448 
	int size=m.size();
	if(size%512!=448){
		m.push_back(1);
		while(m.size()%512!=448){
			m.push_back(0);
		}
	}
	//最后64位填充明文长度
	int h = size,t=m.size();
	int g=0;
	while(1){
		if(h!=0){
			m.insert(m.begin()+t,h%2);
			h=h/2;
		}else{
			m.insert(m.begin()+t,0);
		}
		g++;
		if(g==64)
			break;
	}
	//k赋值
	for(int i=0;i<320;i++){ 
    	if(i%2==0){
    		k.push_back(0);
		}else{
			k.push_back(1);
		}
	}
	//IV赋值 
	for(int i=0;i<160;i++){
    	if(i%16<8){
    		IV.push_back(0);
		}else{
			IV.push_back(1);
		}
	}
	//k左边补0得到k+
	for(int i=0;i<192;i++){
		k.insert(k.begin(),0);
	}
	//得到si 
	for(int i=0,j=0;i<512;i++){
		si.push_back(k[i] ^ ipad[j]);
		j++;
		if(j==8){
			j=0;
		}
	}
	//连接si和明文m
	for(int i=511;i>=0;i--){
		m.insert(m.begin(),si[i]);
	}
	//压缩
	compress_num++;
	Hash(m);
	//填充压缩结果至长度取余512等于448 
	size=M1.size();
	if(size%512!=448){
		M1.push_back(1);
		while(M1.size()%512!=448){
			M1.push_back(0);
		}
	}
	//最后64位填充压缩结果的长度
	h = size;
	g=0;
	t=M1.size();
	while(1){
		if(h!=0){
			M1.insert(M1.begin()+t,h%2);
			h=h/2;
		}else{
			M1.insert(M1.begin()+t,0);
		}
		g++;
		if(g==64)
			break;
	}
	//得到so
	for(int i=0,j=0;i<512;i++){
		so.push_back(k[i] ^ opad[j]);
		j++;
		if(j==8){
			j=0;
		}
	}
	//连接so和第一次压缩后的结果 
	for(int i=511;i>=0;i--){
		M1.insert(M1.begin(),so[i]);
	}
	//压缩 
	compress_num++;
	Hash(M1); 
	//输出最后压缩的结果
	for(int i=0;i<M2.size();i++){
		cout<<M2[i];
		if(i%32==31){
			cout<<endl;
		}
	}
    return 0;
}
