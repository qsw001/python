// 递归写法
#include<iostream>
using namespace std;

int sequence_quantity(int n) {
    if (n == 1) {
        return 1;
    }
    int sum = 0;
    sum++;
    for (int i = 1;i <= n / 2;i++) {
        sum += sequence_quantity(i);
    }
    return sum;
}

int main() {
    int n;
    cin >> n;
    cout<<sequence_quantity(n);
}

// 这是动态规划的写法
#include<iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000] = { 0 };
    a[1] = 1;
    int x = n / 2;//定义要算的数量
    for (int i = 2;i <= x;i++) {
        a[i]++;
        for (int j = 1; j <= i / 2;j++) {
            a[i] += a[j];
        }
    }

    int result = 1;
    for (int i = 1;i <= x;i++) {
        result += a[i];
    }
    cout << result;
}