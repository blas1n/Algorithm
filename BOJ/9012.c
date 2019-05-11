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
void Clear(Stack* stack);

int main() {
	Stack* stack = malloc(sizeof(Stack));
	memset(stack, 0, sizeof(Stack));

	char text[50];
	int t;
	scanf("%d", &t);

	while (t--) {
		scanf("%s", text);

		for (unsigned int i = 0; i < strlen(text); i++) {
			if (text[i] == '(')
				Push(stack);

			else if (text[i] == ')')
				if (Pop(stack) == -1) {
					Push(stack);
					break;
				}

		}

		printf("%s\n", Empty(stack) ? "YES" : "NO");
		Clear(stack);
	}

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

void Clear(Stack* stack) {
	while (!Empty(stack))
		Pop(stack);
}