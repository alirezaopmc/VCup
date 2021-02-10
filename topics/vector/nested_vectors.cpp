#include <iostream>
#include <vector>
// #include <algorithm>
// #include <stack>

using namespace std;

void print2DVector(vector<vector<int>> v);

int main() {
    vector<vector<int>> v(10, vector<int>(20, -2)); // int v[10][20];

    v[7][13] = -1;
    
    print2DVector(v);
    // cout << endl;
    // for(int i=0; i<v.size(); i++) {
    //     for(int j=0; j<v[i].size(); j++) {
    //         cout << v[i][j] << " ";
    //     }
    //     cout << endl;
    // }
}

void print2DVector(vector<vector<int>> v) {
    // v[0][0] = -3;
    for(int i=0; i<v.size(); i++) {
        for(int j=0; j<v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
}