#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int T;

typedef struct _NODE {
	T data;
	struct _NODE* next;
} Node;

typedef struct _STACK {
	Node* head;
	int size;
} Stack;

void Push(Stack* stack);
int Pop(Stack* stack);
int Size(Stack* stack);
int Empty(Stack* stack);
int Top(Stack* stack);

int main() {
	Stack* stack = malloc(sizeof(Stack));
	memset(stack, 0, sizeof(Stack));

	int ans = 0, stick = 0;
	char text[100000];
	scanf("%s", text);

	for (unsigned int i = 0; i < strlen(text); i++) {
		if (text[i] == '(') {
			if (text[i + 1] == ')') {
				ans += Size(stack);
				i++;
				continue;
			}

			Push(stack);
		}

		else if (text[i] == ')') {
			Pop(stack);
			stick++;
		}
	}

	printf("%d\n", ans + stick);
	free(stack);
	return 0;
}

void Push(Stack* stack) {
	Node* node = malloc(sizeof(Node));
	node->data = 0;
	node->next = stack->head;
	stack->head = node;
	stack->size++;
}

int Pop(Stack* stack) {
	if (Empty(stack))
		return -1;

	int ret = Top(stack);

	Node* delNode = stack->head;
	stack->head = delNode->next;
	free(delNode);
	stack->size--;

	return ret;
}

int Size(Stack* stack) {
	return stack->size;
}

int Empty(Stack* stack) {
	return stack->size == 0;
}

int Top(Stack* stack) {
	if (Empty(stack))
		return -1;

	return stack->head->data;
}