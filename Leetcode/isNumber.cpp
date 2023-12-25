#include<iostream>
using namespace std;

class Solution {
public:
    bool isNumber(string s) {
        char*p=&s[0];
        bool isfloat=false;
        bool isexp=false;
        while(p<&s[0]+s.size()&&*p==' ')p++;
        if(*p!='+'&&*p!='-'&&*p!='.'&&!isdigit(*p)) return false;
        if(*p=='+'||*p=='-'){
            if(p==&s[0]+s.size()-1) return false;
            if(*(p+1)!='.'&&!isdigit(*(p+1))) return false;
            else p++;
        }
        if(*p=='.'){
            if(p==&s[0]+s.size()-1) return false;
            if(!isdigit(*(p+1))) return false;
            else p++;
            isfloat=true;
        }
        while(p<&s[0]+s.size()&&isdigit(*p))p++;
        if(p==&s[0]+s.size()) return true;
        else if(*p==' '){
            if(p==&s[0]+s.size()-1) return true;
            while(p<&s[0]+s.size()&&*p==' ')p++;
            //printf("%c",*p);
            if(p==&s[0]+s.size()) return true;
            else return false;
        }else if(!isfloat&*p=='.'){
            if(p==&s[0]+s.size()-1) return true;
            p++;
            if(*p==' '){
                if(p==&s[0]+s.size()-1) return true;
                while(p<&s[0]+s.size()&&*p==' ')p++;
                if(p==&s[0]+s.size()) return true;
                else return false;
            }else if(*p!='e'&&*p!='E'&&!isdigit(*p)) return false;
            else if(*p=='e'||*p=='E'){
                isexp=true;
                if(p==&s[0]+s.size()-1) return false;
                p++;
                if(*p!='+'&&*p!='-'&&!isdigit(*p)) return false;
                if(*p=='+'||*p=='-'){
                    if(p==&s[0]+s.size()-1) return false;
                    if(!isdigit(*(p+1))) return false;
                    else p++;
                }
            }
        }else if(*p=='e'||*p=='E'){
            if(isexp||p==&s[0]+s.size()-1) return false;
            isexp=true;
            p++;
            if(*p!='+'&&*p!='-'&&!isdigit(*p)) return false;
            if(*p=='+'||*p=='-'){
                if(p==&s[0]+s.size()-1) return false;
                if(!isdigit(*(p+1))) return false;
                else p++;
            }
        }else return false;
        while(p<&s[0]+s.size()&&isdigit(*p))p++;
        if(p==&s[0]+s.size()) return true;
        else if(*p==' '){
            if(p==&s[0]+s.size()) return true;
            while(p<&s[0]+s.size()&&*p==' ')p++;
            if(p==&s[0]+s.size()) return true;
            else return false;
        }else if(*p=='e'||*p=='E'){
            if(isexp||p==&s[0]+s.size()-1) return false;
            p++;
            if(*p!='+'&&*p!='-'&&!isdigit(*p)) return false;
            if(*p=='+'||*p=='-'){
                if(p==&s[0]+s.size()-1) return false;
                if(!isdigit(*(p+1))) return false;
                else p++;
            }
        }else return false;
        while(p<&s[0]+s.size()&&isdigit(*p))p++;
        if(p==&s[0]+s.size()) return true;
        else if(p<&s[0]+s.size()&&*p==' ')while(p<&s[0]+s.size()&&*p==' ')p++;
        if(p==&s[0]+s.size()) return true;
        else return false;
    }
};
