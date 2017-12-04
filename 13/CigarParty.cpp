#include <iostream>
using namespace std;

bool cigar_party(int cigars, bool is_weekend) {
	if (is_weekend == true) {
		if (cigars < 40) {
			return false;
		}
		return true;
	}
	if (cigars < 40) {
		return false;
	}
	if (cigars > 60) {
		return false;
	}
	return true;
}

int main() {
	cout << boolalpha;
	cout << "cigar_party(61,false) = " << cigar_party(61,false) << endl;
	cout << "cigar_party(41,false) = " << cigar_party(41,false) << endl;
	cout << "cigar_party(100,true) = " << cigar_party(100,true) << endl;
	return 0;
}