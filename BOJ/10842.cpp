#include <iostream>
#include <string>

using namespace std;

int main() {
	string a, b, c, d;
	cin >> a >> b >> c >> d;

	a.append(b);
	c.append(d);

	cout << atoll(a.c_str()) + atoll(c.c_str()) << endl;
	return 0;
}