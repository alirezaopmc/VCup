#include <iostream>

using namespace std;

string subsub(string s, int n, int m);

int main() {
    // char s[100]; // C
    string s = "aaaafffghmm";

    int n, m;
    cin >> n >> m;
    string t = subsub(s, n, m);

    cout << t << endl;
    cout << s.substr(n, m-n+1);
}

string subsub(string s, int n, int m) {
    string tasdasd;
    
    for(int i=n; i<=m; i++)
        tasdasd += s[i];


    return tasdasd;
}