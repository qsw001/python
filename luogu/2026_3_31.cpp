#include<iostream>
#include<vector>

using namespace std;

int num = 0;

vector<vector<int>> dp(102, vector<int>(10002, 0));

int main() {
    int n, m;//n为菜品种类，m为总价钱
    cin >> n >> m;
    vector<int> value(n+1);
    for (int i = 1;i <= n;i++) {
        cin >> value[i];
    }
    for (int i = 1;i <= n;i++) {
        for (int j = 1;j <= m;j++) {
            if (j == value[i]) {
                dp[i][j] = dp[i - 1][j] + 1;//要么之选i，要么不选i
            }
            if (j > value[i]) {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - value[i]];
            }
            if (j < value[i]) {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << dp[n][m];

    return 0;
}