#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    int a[n];
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }

    long long s = 0;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            // a[i] --> a[j]
            for(int k = i; k <= j; k++) {
                s += a[k];
            }
        }
    }

    cout << s << endl;
}