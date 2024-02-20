#include <iostream>
using namespace std;
void printW(int n){
    if(n== 0) return;
    cout << "HelloWorld" <<"\n";
    printW(n-1);

}

int main() {
    int x;
    cin >> x;
    printW(x);
    // 여기에 코드를 작성해주세요.
    return 0;
}