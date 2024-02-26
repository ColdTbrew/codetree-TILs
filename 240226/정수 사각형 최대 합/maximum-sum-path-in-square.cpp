#include <iostream>
#include <algorithm> // max 함수 사용을 위해 포함
using namespace std;

int map[100][100];
long long dp[100][100];
int n;

void solve() {

    dp[0][0] = map[0][0];


    for(int i = 1; i < n; i++) {
        dp[i][0] = dp[i-1][0] + map[i][0]; // 첫 열
        dp[0][i] = dp[0][i-1] + map[0][i]; // 첫 행
    }


    for(int i = 1; i < n; i++) {
        for(int j = 1; j < n; j++) {
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + map[i][j];
        }
    }


    cout << dp[n-1][n-1] << endl;
}

int main() {
    cin >> n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> map[i][j];
        }
    }

    solve();
    return 0;
}