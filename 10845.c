#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>

#pragma warning(disable:6011)
#pragma warning(disable:6031)
#pragma warning(disable:6387)
#pragma warning(disable:6054)

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
int Front(Queue self);
int Back(Queue self);
int Empty(Queue self);
int Size(Queue self);

int main() {
	Queue queue = New();

	char command[10];
	int n, data;
	scanf("%d", &n);

	while (n--) {
		scanf("%s", command);

		if (!strcmp(command, "push")) {
			scanf("%d", &data);
			Push(queue, data);
			continue;
		}

		if (!strcmp(command, "pop")) {
			printf("%d\n", Pop(queue));
			continue;
		}

		if (!strcmp(command, "front")) {
			printf("%d\n", Front(queue));
			continue;
		}

		if (!strcmp(command, "back")) {
			printf("%d\n", Back(queue));
			continue;
		}

		if (!strcmp(command, "empty")) {
			printf("%d\n", Empty(queue));
			continue;
		}

		if (!strcmp(command, "size")) {
			printf("%d\n", Size(queue));
			continue;
		}
	}

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

int Front(Queue self) {
	if (Empty(self))
		return -1;

	return self->front->data;
}

int Back(Queue self) {
	if (Empty(self))
		return -1;

	return self->rear->data;
}

int Empty(Queue self) {
	return self->size == 0;
}

int Size(Queue self) {
	return self->size;
}