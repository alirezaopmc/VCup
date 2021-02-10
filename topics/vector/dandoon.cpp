#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> v(n);

    for(int i = 0; i < n; i++) {
        int m;
        cin >> m;
        v[i] = vector<int>(m);
        for(int j = 0; j < m; j++) {
            cin >> v[i][j];
        }
    }
    
    for(int i = 0; i < n; i++) {
        int m = v[i].size();
        for(int j = 0; j < m; j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}