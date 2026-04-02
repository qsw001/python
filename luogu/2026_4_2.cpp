#include<iostream>
#include<string>
using namespace std;

int main() {
    string s;
    long long N ,L;
    cin >> s >> N;
    L = s.length();
    long long x = L;
    while (L < N) {
        L = L * 2;
    }
    while (N > x) {
        if (N > L / 2) {
            N = (N - 1) % (L / 2);
            if (N == 0) {
                N = L / 2;
            }
        }
        L = L / 2;
    }
    cout << s[N-1];

    return 0;
}

