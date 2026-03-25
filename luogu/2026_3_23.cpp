#include<iostream>
using namespace std;

int stack_algroth(int n) {
    if (n == 0) {
        return 1;
    }

    int sum = 0;

    for (int i = 1;i <= n;i++) {
        sum += stack_algroth(i - 1) * stack_algroth(n - i);
    }

    return sum;
}

int main() {
    int n;
    cin >> n;
    cout<<stack_algroth(n);

    return 0;
}