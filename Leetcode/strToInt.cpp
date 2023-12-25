#include<iostream>
using namespace std;

class Solution {
public:
    int strToInt(string str) {
        long res = 0;
        bool negative = false;
        int i = 0;
        while(str[i] == ' ')
        i++;
        if(!isdigit(str[i]) && str[i] != '+' && str[i] != '-')
            return 0;
        if(str[i] == '-'){
            negative = true;
            i++;
        }
        else if(str[i] == '+') i++;
        while(isdigit(str[i])){
            res = res * 10 + str[i] - '0';
            if(negative == false && res > INT_MAX)
                return INT_MAX;
            else if(negative == true && -res < INT_MIN)
                return INT_MIN;
            i++;
        }
        return negative?-res:res;
    }
};