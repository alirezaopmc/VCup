#include <iostream>

using namespace std;

int main() {
    string s;
    cin >> s;
    
    for(int i=0; i<s.size(); i++) {
        int d = s[i] - '0';
        
        for(int j=0; j<d; j++) {
            cout << s[i];
        }
    }
}