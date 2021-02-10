#include <iostream>

using namespace std;

const int N = 1e6;
int fibo[N]; // 0
bool flag[N]; // false = 0

int f(int n);

int main() {
    flag[0] = flag[1] = true;
    fibo[0] = 0;
    fibo[1] = 1;

    int n;
    cin >> n;

    cout << f(n) << endl;
}

int f(int n) {
    if (flag[n]) return fibo[n];
    flag[n] = true;
    
    return fibo[n] = f(n-1) + f(n-2);
}