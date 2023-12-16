#include <stdio.h>
int ngong(int x, int y);

void main() {
	printf("ngong(28, 16) = %d\n", ngong(28, 16));
	printf("ngong(19, 9) = %d\n", ngong(19, 9));
	printf("ngong(25, 45) = %d\n", ngong(25, 45));
	printf("ngong(49, 63) = %d\n", ngong(49, 63));
	printf("ngong(100, 80) = %d\n", ngong(100, 80));
	printf("flag{md5(ngong(432978, 499226, 898261))}\n");
}

int ngong(int x, int y) {
    if (x < y) {
		return ngong(y, x);
    } else if (x % y == 0) {
		return y;
    } else {
		return ngong(y, x % y);
	}
}