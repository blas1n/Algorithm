#include <string>
#include <vector>

using namespace std;

int dayNum[12] = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
string day[7] = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };

string solution(int a, int b) {
	for (int i = 2; i <= a; i++)
		b += dayNum[i - 2];

	return day[(b - 1) % 7];
}