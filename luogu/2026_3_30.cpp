#include<iostream>
#include<vector>
using namespace std;

vector<vector<int>> a(1010, vector<int>(1010, 0));

vector<int> add_big(vector<int> a, vector<int> b) {
    int i, j;
    vector<int> c(1010);
    int sum = 0;
    i = 1;
    j = 1;
    int index = 1;
    int carry = 0;
    while (i < a.size() && j < b.size()) {
        sum = a[i++] + b[j++] + carry;
        carry = sum / 10;
        c[index++] = (sum) % 10;
    }
    return c;
}

vector<int> f(int x) {
    if (x == 2) {
        return a[2];
    }
    if (x == 3) {
        return a[3];
    }
    if (a[x][1]!=0) {
        return a[x];
    }
    return a[x] = add_big(f(x - 1), f(x - 2));
}

int main() {
    int m, n;
    cin >> m;
    cin >> n;
    int x = n - m + 1;
    a[2][1] = 1;
    a[3][1] = 2;
    vector<int> ans = f(x);
    int len=ans.size()-1;
    while (len > 0 && ans[len] == 0) {
        //找到最高位
        len--;
    }
    for (int i = len;i > 0;i--) {
        cout << ans[i];
    }
    return 0;
}