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
        if(input =='L'){
            it--;
        }
        if(input =='R'){
            it++;
        }
        if(input =='D'){
            l.erase(it);
        }
        if(input =='P'){
            char x;
            cin >> x;
            l.insert(it, x);
            it++
        }
    }
    for(it = l.begin(); it != l.end(); it++) {
        cout << *it;      
    }   

    return 0;
}