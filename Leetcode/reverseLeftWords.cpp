#include<iostream>
using namespace std;

class Solution {
public:
    string reverseLeftWords(string s, int n) {
       return s.substr(n)+s.substr(0,n);
    }
};