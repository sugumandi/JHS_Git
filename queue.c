#define MAX_QUEUE_SIZE 10 //���� ť�� ť�� ������� 1�� ���� ������ �����͸� ������ �� �ִ�.
#define NAME_LENGTH 20
#include <stdio.h>
#include <string.h>

char queue[MAX_QUEUE_SIZE][NAME_LENGTH+1];
int rear = 0, front = 0;
char nameofpat[NAME_LENGTH+1];
void addq()
{
	if (front == ((rear + 1)% MAX_QUEUE_SIZE))
	{
		printf("Full\n");
		return 0;
	}
	rear = (rear + 1) % MAX_QUEUE_SIZE;
	printf("Add data(string): ");
	scanf("%s", nameofpat);
	strcpy(queue[rear], nameofpat);
}

void deletq()
{
	if (front == rear)
	{
		printf("Nothing. ---------");
		return 0;
	}
	front = (front + 1) % MAX_QUEUE_SIZE;
	printf("%s\n\n", queue[front]);
}