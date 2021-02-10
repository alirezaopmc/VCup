#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> v(n);

    for(int i = 0; i < n; i++) { // iteration with number
        cin >> v[i];
    }

    for(int x : v) { // iteration with reference
        cout << x << endl;
    }
}