#include <string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    int pNum = 0, yNum = 0;

	for (auto c : s) {
		if (c == 'Y' || c == 'y')
			yNum++;
		else if (c == 'P' || c == 'p')
			pNum++;
	}

	return pNum == yNum;
}