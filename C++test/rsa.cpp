#include <iostream>
#include <cstdlib>
#include <ctime>
 
// 素性检测算法（使用米勒-拉宾算法作为示例）
bool isPrime(int n, int k) {
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
 
    int d = n - 1;
    int r = 0;
    while (d % 2 == 0) {
        d = d / 2;
        r++;
    }
 
    for (int i = 0; i < k; i++) {
        int a = 2 + rand() % (n - 3);
 
        int x = 1;
        for (int j = 0; j < d; j++) {
            x = (x * a) % n;
        }
 
        if (x == 1 || x == n - 1)
            continue;
 
        bool isComposite = true;
        for (int j = 0; j < r - 1; j++) {
            x = (x * x) % n;
            if (x == 1)
                return false;
            if (x == n - 1) {
                isComposite = false;
                break;
            }
        }
 
        if (isComposite)
            return false;
    }
 
    return true;
}
 
// 扩展的欧几里得算法
int extendedEuclidean(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
 
    int x1, y1;
    int gcd = extendedEuclidean(b, a % b, x1, y1);
 
    x = y1;
    y = x1 - (a / b) * y1;
 
    return gcd;
}
 
// RSA加密
int rsaEncrypt(int message, int e, int n) {
    int ciphertext = 1;
    for (int i = 0; i < e; i++) {
        ciphertext = (ciphertext * message) % n;
    }
    return ciphertext;
}
 
// RSA解密
int rsaDecrypt(int ciphertext, int d, int n) {
    int message = 1;
    for (int i = 0; i < d; i++) {
        message = (message * ciphertext) % n;
    }
    return message;
}
 
int main() {
    // 设置随机数种子
    srand(time(0));
 
    // 生成3位数的素数
    int prime;
    do {
        prime = 100 + rand() % 900;
    } while (!isPrime(prime, 10));
 
    std::cout << "Generated prime: " << prime << std::endl;
 
    // 选择公钥e
    int e = 7;
 
    // 计算私钥d
    int d, x, y;
    int phiN = prime - 1;
    extendedEuclidean(e, phiN, x, y);
    d = x;
    if (d < 0)
        d += phiN;
 
    std::cout << "Public key (e, n): (" << e << ", " << prime << ")" << std::endl;
    std::cout << "Private key (d, n): (" << d << ", " << prime << ")" << std::endl;
 
    // 选择明文m
    int m = 123;
 
    // 加密
    int ciphertext = rsaEncrypt(m, e, prime);
 
    std::cout << "Ciphertext: " << ciphertext << std::endl;
 
    // 解密
    int decryptedMessage = rsaDecrypt(ciphertext, d, prime);
 
    std::cout << "Decrypted message: " << decryptedMessage << std::endl;
 
    return 0;
}