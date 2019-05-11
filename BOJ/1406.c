#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _SCROLL {
	char data[600000];
	int lPos;
	int rPos;
} Scroll;

void Push(Scroll* pScroll, char c);
char LPop(Scroll* pScroll);
char RPop(Scroll* pScroll);
int Size(Scroll* pScroll);
int Empty(Scroll* pScroll);

int main() {
	Scroll* left = (Scroll*)malloc(sizeof(Scroll));
	memset(left, 0, sizeof(Scroll));

	Scroll* right = (Scroll*)malloc(sizeof(Scroll));
	memset(right, 0, sizeof(Scroll));

	char command, text;
	int t;

	scanf("%s", left->data);
	left->rPos = strlen(left->data);

	scanf("%d", &t);

	while (t--) {
		scanf(" %c", &command);

		switch (command) {
		case 'L':
			Push(right, LPop(left));
			break;

		case 'D':
			Push(left, LPop(right));
			break;

		case 'B':
			LPop(left);
			break;

		case 'P':
			scanf(" %c", &text);
			Push(left, text);
			break;
		}
	}

	while (!Empty(left))
		putchar(RPop(left));

	while (!Empty(right))
		putchar(LPop(right));

	return 0;
}

void Push(Scroll* pScroll, char c) {
	if (c != 0)
		pScroll->data[pScroll->rPos++] = c;
}

char LPop(Scroll* pScroll) {
	if (Empty(pScroll)) return 0;
	return pScroll->data[--pScroll->rPos];
}

char RPop(Scroll* pScroll) {
	if (Empty(pScroll)) return 0;
	return pScroll->data[pScroll->lPos++];
}

int Size(Scroll* pScroll) {
	return pScroll->rPos - pScroll->lPos;
}

int Empty(Scroll* pScroll) {
	return Size(pScroll) == 0;
}