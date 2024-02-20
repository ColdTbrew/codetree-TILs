#include <iostream>
using namespace std;
void counter(int n){
    if(n== 0) return;
    counter(n-1);
    cout << n <<" ";
}
void counter2(int n){
    if(n== 0) return;
    cout << n <<" ";
    counter2(n-1);
}
int main() {
    int x;
    cin >> x;
    counter(x);
    cout << "\n";
    counter2(x);
    // 여기에 코드를 작성해주세요.
    return 0;
}