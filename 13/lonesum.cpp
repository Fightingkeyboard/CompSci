#include <iostream>
using namespace std;

int lone_sum (int a, int b, int c) {
	if (a == b ) {
		if (a == c) {
			return 0;
		}
		else {
			return c;
		}
	}
	if (a == c) {
		return b;
	}
	if (b == c) {
		return a;
	}
	return a + b + c;
}

int main() {
	cout << "lone_sum 1,1,2 = " << lone_sum(1,1,2) << endl;
	cout << "lone_sum 1,3,2 = " << lone_sum(1,3,2) << endl;
	cout << "lone_sum 2,2,2 = " << lone_sum(2,2,2) << endl;
}