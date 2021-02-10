#include <iostream>
#include <vector>
// #include <algorithm>
// #include <stack>

using namespace std;

int main() {
    // int n;
    // cin >> n;
    // int a[n];

    // for(int i=0; i<n; i++) {
    //     // a[i]
    // }

    // vector<T> a;
    // T a[?];
    vector<int> v;
    v.push_back(12);
    v.push_back(5);
    v.push_back(1);
    
    for(int i=0; i < v.size(); i++) {
        printf("%d ", v[i]);
    }
    cout << endl;
    printf("\n");
    v[2] = 13;
    
    for(int i=0; i < v.size(); i++) {
        printf("%d ", v[i]);
    }
}