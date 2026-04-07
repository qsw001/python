#include<iostream>
#include<string>

using namespace std;

string s;

//把i移到j上,并移动下一位
void move(int i, int j) {
    char ch;
    ch = s[i];
    s[i] = s[j];
    s[j] = ch;
    ch = s[i + 1];
    s[i + 1] = s[j + 1];
    s[j + 1] = ch;
    cout << s << endl;
}

void f(int n) {
    if (n == 4) {
        move(3, 8);
        move(3, 7);
        move(1, 7);
        move(1, 6);
        move(0, 6);
    }
    else {
        move(n - 1, 2 * n);
        move(n - 1, 2 * n - 2);
        f(n - 1);
    }
}

int main() {
    int n;
    cin >> n;
    s.resize(2 * n + 2);
    for (int i = 0; i < n;i++) {
        s[i] = 'o';
    }
    for (int i = n;i < 2 * n;i++) {
        s[i] = '*';
    }
    s[2 * n] = '-';
    s[2 * n + 1] = '-';
    cout << s << endl;
    f(n);

    return 0;
}
