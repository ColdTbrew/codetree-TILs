#include <iostream>
using namespace std;
void recur(int x){
    if(x==0){
        return;
    }
    cout << x <<" ";
    recur(x-1);
    cout << x <<" ";
}
int main() {
    int x;
    cin >> x;
    recur(x);
    // 여기에 코드를 작성해주세요.
    return 0;
}