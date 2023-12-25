/*
 * @Descripttion: 
 * @version: 
 * @Author: Ryan
 * @Date: 2023-11-06 14:52:24
 * @LastEditors: Ryan
 * @LastEditTime: 2023-11-06 14:52:49
 */
#include <iostream>
long long fastExponentiation(long long base, long long exponent, long long modulus){
	long long result = 1;
	base = base % modulus;
	
	while (exponent > 0){
		if (exponent % 2 == 1)
			result = (base * result) % modulus;
		base = (base * base) % modulus;
		exponent /= 2;
	}
	return result;
}
 
int main(){
	long long base = 7560;
	long long exponent = 561;
	long long modulus = 561;
	
	long long result = fastExponentiation(base, exponent, modulus);
	
	std::cout << base << " raised to the power of " << exponent << "( mod " << modulus << ") is: "<< result << std::endl;
	
	return 0;
}
