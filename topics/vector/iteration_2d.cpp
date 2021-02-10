#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    // <Generic>
    vector<vector<int>> v(n, vector<int>(m));

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> v[i][j];
        }
    }

    // auto f = 1.2F;
    // auto a = 222LL;

    for(auto x : v) { // x is vector<int>
        for(int p : x) {
            cout << p << " ";
        }
        cout << endl;
    }
}