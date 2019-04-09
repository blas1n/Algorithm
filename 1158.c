#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

typedef struct _NODE {
	int data;
	struct _NODE* next;
} _Node, *Node;

typedef struct _QUEUE {
	Node front;
	Node rear;
	int size;
} _Queue, *Queue;

Queue New();
void Delete(Queue self);
void Push(Queue self, int data);
int Pop(Queue self);
int Empty(Queue self);
int Size(Queue self);

int main() {
	Queue queue = New(); 
	
	int n, k, i;
	scanf("%d %d", &n, &k);

	for (i = 1; i <= n; i++)
		Push(queue, i);

	printf("<");

	while (1) {
		for (i = 0; i < n; i++) {
			if (i + 1 == k) {
				printf("%d", Pop(queue));
				break;
			}
			
			Push(queue, Pop(queue));
		}

		if (Size(queue) <= 1) {
			if (Empty(queue))
				break;
		}

		printf(", ");
	}

	printf(">");

	Delete(queue);
	return 0;
}

Queue New() {
	Queue instance = malloc(sizeof(_Queue));
	memset(instance, 0, sizeof(_Queue));
	return instance;
}

void Delete(Queue self) {
	while (Pop(self) != -1);
	free(self);
}

void Push(Queue self, int data) {
	Node node = malloc(sizeof(_Node));
	node->data = data;
	node->next = NULL;

	if (Empty(self)) {
		self->front = self->rear = node;
	}

	else {
		self->rear->next = node;
		self->rear = node;
	}

	self->size++;
}

int Pop(Queue self) {
	if (!self->front)
		return -1;

	Node delNode = self->front;
	self->front = delNode->next;

	int ret = delNode->data;
	free(delNode);
	self->size--;
	return ret;
}

int Empty(Queue self) {
	return self->size == 0;
}

int Size(Queue self) {
	return self->size;
}