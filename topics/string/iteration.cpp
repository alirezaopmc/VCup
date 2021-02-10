#include <iostream>
#include <vector>

using namespace std;

int main() {
    string s = "abc harf mizani";

    for(auto c : s) {
        cout << (char)(c+1);
    }
}