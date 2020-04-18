#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n >> m;  // read n and then m.
    int houses[10^6];
    for(int j = 0; j < n; j++){
    	cin >> houses[j];
    }
    sort(houses, houses+n);
    int total, count;
    total = count = 0;

    while(total < m){
    	total = total + houses[count];
    	if(total <= m){
    		count++;
    	}
    }
    cout << "Case " << i << ": " << count << endl;

    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

  return 0;
}