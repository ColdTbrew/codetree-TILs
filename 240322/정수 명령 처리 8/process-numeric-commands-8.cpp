#include <iostream>
#include <list>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    list<int> l;
    int n;
    cin >> n;
    while(n--){
        string input;
        cin >> input;
        if(input=="push_back"){
            int x;
            cin >> x;
            l.push_back(x);
        }
        if(input=="push_front"){
            int x;
            cin >> x;
            l.push_front(x);
        }
        if(input=="pop_front"){
            int x = l.front();
            l.pop_front();
            cout << x;
            cout << "\n";
        }
        if(input=="pop_back"){
            int x = l.back();
            l.pop_back();
            cout << x;
            cout << "\n";
        }
        if(input=="size"){
            cout << l.size();
            cout << "\n";
        }
        if(input=="empty"){
            cout << l.empty();
            cout << "\n";

        }
        if(input=="front"){
            cout << l.front();
            cout << "\n";
        }
        if(input=="back"){
            cout <<l.back();
            cout << "\n";
        }
        
    }
    return 0;
}