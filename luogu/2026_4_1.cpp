#include<iostream>
#include<vector>

using namespace std;

int main() {
    vector<int> f(1000002);
    vector<int> g(1000002);
    f[1] = 1;
    f[2] = 2;
    g[2] = 1;
    g[3] = 2;
    
    int N;
    cin >> N;

    for (int i = 3;i <= N;i++) {
        f[i] = (f[i - 1] + f[i - 2] + 2 * g[i - 1])%10000;
        g[i] = (f[i - 2] + g[i - 1])%10000;
    }

    cout << f[N];

    return 0;
}