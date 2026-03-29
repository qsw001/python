#include<iostream>
#include<string>

using namespace std;

string f() {
    int k;
    char ch;
    string res_str="";
    string ret_str="";

    while (cin >> ch) {
    
        //调用递归条件
        if (ch == '[') {
            cin >> k;
            ret_str = f();
            while (k--) {
                res_str += ret_str;
            }
        }
        else if (ch == ']') {
            return res_str;
        }
        else {
            res_str += ch;
        }
    }
    return res_str;
}

int main() {
    cout << f();

    return 0;
}