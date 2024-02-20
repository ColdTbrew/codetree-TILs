#include <iostream>
using namespace std;

void printer(int n){
    if(n==0) return;
    printer(n-1);
    for(int i =0;i < n;i++){
        cout << "*";
    }
    cout << "\n";
}
int main() {
    // 여기에 코드를 작성해주세요.
    int x;
    cin >> x;
    printer(x);
    return 0;
}