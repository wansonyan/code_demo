/*
 * @Descripttion: 
 * @version: 
 * @Author: Ryan
 * @Date: 2023-05-25 20:30:34
 * @LastEditors: Ryan
 * @LastEditTime: 2023-05-25 20:30:50
 */
#include<iostream>
using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        int size = s.size();
        for(int i = 0;i < size;i++){
            if(s[i] == ' '){
                s.insert(i,"%20");
                i+=2;
                s.erase(i+1,1);
                size+=2;
            }
        }
        return s;
    }
};