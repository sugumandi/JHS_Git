#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
typedef struct tree_node
{
	struct treenode* left;
	int data;
	struct treenode* right;
}tree_node;

tree_node* root = NULL;

int *inorderorder, count = 0, i = 0;

tree_node *search(tree_node* node, int a) //Ʈ������ Ư�� ���� ���� ��带 ã��, �� ����� �ּҸ� ��ȯ�ϴ� �Լ�
{
	if (node == NULL)
	{
		return NULL;
	}
	else if (node->data == a) {
		return node;
	}
	else {
		tree_node *target = search(node->left, a);
		if (target != NULL)
			return target;
		return search(node->right, a);
	}
}

void insert_Root()
{
	if (root == NULL)
	{
		int rootdata;
		root = (tree_node*)malloc(sizeof(tree_node));
		root->left = NULL;
		root->right = NULL;
		printf("Enter the root node information: ");
		scanf("%d", &rootdata);
		printf("\n");
		root->data = rootdata;
		printf("The root node is %d\n\n", rootdata);
		count++;
	}
	else
	{
		printf("Error: This is not an empty binary tree.\n\n");
	}
}

int insert_Left()
{
	if (root == NULL) //Ʈ���� ���µ� ���� �ڽ� ��� �߰��Ϸ��� ��� ���� �޽���
	{
		printf("There is no tree.\n\n");
		return 0;
	}
	int parent, left_data;
	tree_node* parent_addr;
	printf("Enter the parent information: ");
	scanf("%d", &parent);
	printf("\n");
	parent_addr = search(root, parent);
	tree_node* left_child;
	left_child = (tree_node*)malloc(sizeof(tree_node));
	printf("Enter the left child information: ");
	scanf("%d", &left_data);
	printf("\n");
	left_child->data = left_data;
	printf("The left child is %d\n\n", left_child->data);
	left_child->left = NULL;
	left_child->right = NULL;
	parent_addr->left = left_child;
	count++;
}

int insert_Right()
{
	if (root == NULL) //Ʈ���� ���µ� ������ �ڽ� ��� �߰��Ϸ��� ��� ���� �޽���
	{
		printf("There is no tree.\n\n");
		return 0;
	}
	int parent, right_data;
	tree_node* parent_addr;
	printf("Enter the parent information: ");
	scanf("%d", &parent);
	printf("\n");
	parent_addr = search(root, parent);
	tree_node* right_child;
	right_child = (tree_node*)malloc(sizeof(tree_node));
	printf("Enter the right child information: ");
	scanf("%d", &right_data);
	printf("\n");
	right_child->data = right_data;
	printf("The right child is %d\n\n", right_child->data);
	right_child->left = NULL;
	right_child->right = NULL;
	parent_addr->right = right_child;
	count++;
}

tree_node* inorder_Succ(tree_node* node, int value)
{
	inorderorder = (int*)malloc(sizeof(int) * count); //����� ���� inorder travesal�� ������� ������ �迭
	inorder_Succ_helper(node);
	i = 0;
	for (int j = 0; j < count; j++)
	{
		if (inorderorder[j] == value)
		{
			if (j == count-1) //�Է� ���� inorder travesal�� ������ ������ ��� ó��
			{
				return NULL;
			}
			tree_node* successor_node = search(node, inorderorder[j + 1]); 
			return successor_node;
			//�Է� ���� ���� ��(successor)�� ���� ��带 ã�Ƽ� ��ȯ
		}
	}
}

int inorder_Succ_helper(tree_node* node) //�迭�� inorder travesal ������� ��� ���� �迭�� ��� ���� �Լ�
{
	if (node == NULL)
		return;
	else
	{
		inorder_Succ_helper(node->left);
		inorderorder[i] = node->data;
		i++;
		inorder_Succ_helper(node->right);
	}
}

void inorder_Trav(tree_node* node)
{
	if (node == NULL)
		return;
	else
	{
		inorder_Trav(node->left);
		printf("%d ", node->data);
		inorder_Trav(node->right);
	}
}


int main()
{
	int choice;
	while (1)
	{
		printf("Binary tree functions: Select the function you like to proceed with,\n\n");
		printf("	1. Insert root\n\n");
		printf("	2. Insert left\n\n");
		printf("	3. Insert right\n\n");
		printf("	4. Inorder Successor\n\n");
		printf("	5. Inorder Travesal\n\n");
		printf("Selection choice: ");
		scanf("%d", &choice);
		printf("\n");
		if (choice == 1)
		{
			insert_Root();
		}
		else if (choice == 2)
		{
			insert_Left();
		}
		else if (choice == 3)
		{
			insert_Right();
		}
		else if (choice == 4)
		{
			if (root == NULL) //Ʈ���� ���µ� inorder travesal�� ���� ���� ã������ ��� ���� �޽���
			{
				printf("There is no tree.\n\n");
				continue;
			}
			int value;
			printf("Enter the node which you want to find the successor: ");
			scanf("%d", &value);
			printf("\n");
			tree_node *next = inorder_Succ(root, value);
			if (next == NULL)
			{
				printf("There is no successor of %d in this tree\n\n", value);
			}
			else
			{
				printf("The inorder successor of %d is %d\n\n", value, next->data);
			}
		}
		else if (choice == 5)
		{
			printf("The inorder traversal of the tree is ");
			inorder_Trav(root);
			printf("\n\n");
			break;
		}
	}
}