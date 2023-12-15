#include <iostream>
#include <string>
using namespace std;
int main () {
	unsigned int flag[] = { 754, 708, 734, 729, 651, 714, 709, 728, 732, 718, 729, 651, 706, 728, 651, 717, 711, 714, 716, 720, 713, 712, 670, 667, 665, 665, 658, 718, 712, 666, 719, 670, 714, 712, 666, 668, 712, 667, 714, 714, 659, 671, 713, 719, 667, 659, 659, 666, 668, 718, 713, 666, 726 };
    unsigned int key, code, i;
    cout << "Key: ";
    cin >> key;
	for(i = 0; i < 53; i++) {
		code = flag[i] ^ key;
		cout << (char) code;
	}
	cout << endl;
	return 0;
}
