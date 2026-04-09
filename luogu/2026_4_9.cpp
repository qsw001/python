#include<iostream>
#include<math.h>
using namespace std;

void f(int x) {
    if (x == 2) {
        cout << '2';
        return;
    }
    if (x == 1) {
        cout << "2(0)";
        return;
    }
    int y = 0;
    int sum = x;//记录是否算完
    while (y != x) {
        int num = 0;
        ////算出2的幂次方
        while (pow(2, num++) <= sum);
        num = num - 2;
        //更新
        y += pow(2, num);
        sum = x - y;//算剩下的数字
        //大印
        if (num == 1) {
            cout << "2";
            if (y != x) {
                cout << "+";
            }
            continue;
        }
        if (num == 0) {
            cout << "2(0)";
            if (y != x) {
                cout << "+";
            }
            continue;
        }
        cout << "2(";
        f(num);
        cout << ")";
        if (y != x) {
            cout << "+";
        }
    }
}

int main() {
    int x;
    cin >> x;
    f(x);

    return 0;
}