#include <iostream>
using namespace std;
int map[100][100];
long long dp[100][100];
int n;
void solve(){
    dp[1][1] = map[1][1];
    for(int i =1 ;i<=n;i++){
        for(int j = 1;j<= n;j++){
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