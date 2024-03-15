#include <iostream>
#include <vector>
using namespace std;
vector<int> v;
int main() {
    int n;
    cin >> n;
    while(n--){
        string input;
        cin >> input;
        
        if(input== "push_back"){
            int x;
            cin >> x;
            v.push_back(x);
            //cout << x;
        }
        if(input== "get"){
            int x;
            cin >> x;
            cout << v[x-1];
            cout <<"\n";
        }
        if(input== "size"){
            cout << v.size();
            cout <<"\n";
        }
        if(input== "pop_back"){
            v.pop_back();
        }
        
    }
    // 여기에 코드를 작성해주세요.
    return 0;
}