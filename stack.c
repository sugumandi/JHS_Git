#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STACK_SIZE 100

char stack[MAX_STACK_SIZE];
int top = -1;
int index = 0;
void push(int item) {
    if (top == MAX_STACK_SIZE - 1) {
        printf("The stack is full. Pop out the data from the stack.\n");
        return 0;
    }
    stack[++top] = item;
}

char pop() {
    else if (top == -1) {
        printf("The Stack is now empty, continue scanning.\n\n");
        return 0;
    }
    return stack[top--];
}