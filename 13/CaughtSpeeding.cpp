#include <iostream>
using namespace std;

int caught_speeding (int speed, bool is_birthday) {
	if (is_birthday == true) {
		if (speed < 66) {
			return 0;
		}
		else if (speed > 85) {
			return 2;
		}
		return 1;
	}
	else if (speed < 61) {
		return 0;
	}
	else if (speed > 80) {
		return 2;
	}
	return 1;
}

int main() {
	cout << "caught_speeding (85,true) = " << caught_speeding(85, true) << endl;
	cout << "caught_speeding (5,false) = " << caught_speeding(5,false) << endl;
	cout << "caught_speeding (500,false) = " << caught_speeding(500,false) << endl;
	cout << "caught_speeding (75,false) = " << caught_speeding(75,false) << endl;
	return 0;
}