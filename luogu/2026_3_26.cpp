// 对于此题的感悟
//递归的运行不是并行的，而是对于递归树的某种遍历方式(沿着一条方向走到底)，在此途中，每一个结果只需计算一次便存入了dp数组中

#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

long long dp[21][21][21] = { };
bool vis[21][21][21];

long long w(long long a, long long b, long long c) {
    if (a <= 0 || b <= 0 || c <= 0) {
        return 1;
    }
    if (a > 20 || b > 20 || c > 20) {
        return w(20, 20, 20);
    }
    if (vis[a][b][c]) return dp[a][b][c];
    if (a < b && b < c) {
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
    }
    else {
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
    }

    vis[a][b][c] = true;

    return dp[a][b][c];
}

int main() {
    vector<tuple<long long, long long, long long>> data;
    long long a, b, c;
    while (cin >> a >> b >> c) {
        if (a == -1 && b == -1 && c == -1) break;
        cout << "w(" << a << "," << " " << b << "," << " " << c << ")" << " " << "=" << " " << w(a, b, c) << '\n';
    }

    return 0;
}