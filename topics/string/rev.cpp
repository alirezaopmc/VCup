#include <iostream>

using namespace std;

string alireza_rev(string s);

int main() {
    // char s[100]; // C
    string s = "aaaafffghmm";
    
    cout << alireza_rev(s);
}

string alireza_rev(string s) {
    string t;
    int n = s.size();
    // for(int i=0; i<n; i++)
    //     t += s[n-i-1];
    for(int i=n-1; i>=0; i--)
        t += s[i];

    return t;
}