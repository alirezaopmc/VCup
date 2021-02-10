#include <iostream>
#include <string>

using namespace std;

void f(string s);
char up(char c);
char low(char c);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int n;
    cin >> n;
    string s;
    cin.ignore();
    for(int i = 0; i < n; i++) {
        getline(cin, s);
        f(s);
    }
}

void f(string s) {
    for(int i = 0; i < s.size(); i++) {
        if (i == 0 || s[i-1] == ' ') {
            cout << up(s[i]);
        } else {
            cout << low(s[i]);
        }
    }
    cout << endl;
}

char up(char c) {
    if (c >= 'a' && c <= 'z') c = 'A' + c - 'a';
    return c;
}

char low(char c) {
    if (c >= 'A' && c <= 'Z') c = 'a' + c - 'A';
    return c;
}