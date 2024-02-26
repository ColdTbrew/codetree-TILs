#include <iostream>
using namespace std;
int map[100][100];
long long dp[100][100];
int n;
void solve(){
    dp[1][1] = map[1][1];
    for(int i = 1; i < n; i++) {
        dp[i][0] = dp[i-1][0] + map[i][0]; // 첫 열
        dp[0][i] = dp[0][i-1] + map[0][i]; // 첫 행
    }
    for(int i =1 ;i<n;i++){
        for(int j = 1;j< n;j++){
            dp[i][j] = max(dp[i-1][j] + map[i][j],dp[i][j-1] + map[i][j]);
        }
    }
    cout << dp[n][n];
}
int main() {
    cin >> n;
    for(int i =1 ;i<=n;i++){
        for(int j = 1;j<=n;j++){
            cin >> map[i][j];
        }
    }
    solve();
    return 0;
}