#include <iostream>
#include <vector>
// #include <algorithm>
// #include <stack>

using namespace std;

int main() {
    vector<int> v(10, -1); // int v[10];
    // push_back: insert a new element // high time complexity
    // pop_back: remove the last element

    for(int i=0; i<v.size(); i++) {
        cout << v[i] << " ";
    }

    cout << v.size() << endl;
}