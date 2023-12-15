#include <iostream>
using namespace std;
int jeng(int n);

int main() {
	cout << "jeng(n) = 187072209578355573530071658587684226515959365500928" << endl;
	cout << "flag{md5(n * 1919)}" << endl;
	return 0;
}

int jeng(int n) {
    if (n <= 0) {
        return 1;
    } else {
        return jeng(n - 1) + jeng(n - 1);
    }
}
