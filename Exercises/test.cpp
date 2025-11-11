#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n; cin >> n;    // size of the array

    // read input array
    vector<int> arr(n);
    for (auto &x : arr) cin >> x;

    // convert even -> 1, odd -> 0
    for (int i = 0; i < n; i++) {
        arr[i] = (arr[i] % 2 == 0) ? 1 : 0;
    }

    // find position of the last leading zero (if any)
    int initial_zero = -1;
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            initial_zero = i;
        } else {
            break;
        }
    }

    // Build answer string from remaining elements
    string ans;
    for (int i = initial_zero + 1; i < n; i++) {
        ans += char(arr[i] + '0');
    }

    cout << ans << "\n";
}

int32_t main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t; 
    cin >> t;  // number of test cases

    for (int i = 1; i <= t; i++) {
        cout << "Case " << i << ": ";
        solve();
    }

    return 0;
}