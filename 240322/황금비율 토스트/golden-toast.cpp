#include <iostream>
#include <list>
using namespace std;

int main() {
    list<char> l;
    list<char>::iterator it;

    int n, m;
    cin >> n >> m;
    while(n--){
        char c;
        cin >> c;
        l.push_back(c);
    }
    it = l.end();
    while(m--){
        char input;
        cin >> input;
        if(input =='L'&& it != l.begin()){
            it--;
        }
        if(input =='R'&& it != l.end()){
            it++;
        }
        if(input =='D'&& it != l.end()){
            it = l.erase(it);
        }
        if(input =='P'){
            char x;
            cin >> x;
            l.insert(it, x);
        }
    }
    for(auto elem : l) {
        cout << elem;
    }
    cout <<"\n";
    return 0;
}