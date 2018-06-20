#include <stdio.h>
#include <stdlib.h>

// define a struct that is a list "node" (entry in a list) it
// contains and int and a pointer to the next entry in the list 
typedef struct node 
{
	// the data itself
	int data;
	// the "next" element in list
	struct node* next;
} node;

// function to create new nodes 
node* create(int data, node* next)
{
	// allocate memory for the size of a node 
	node* new_node  = (node*)malloc(sizeof(node));
	new_node -> data = data;
	// where the node after will be if it is created
	new_node -> next;

	return new_node;
}

// a function to add an int to the end of a list 
void append(node* head, int data)
{
	node *cursor = head;
	// while you're not at the end, advance 
	while(cursor -> next != NULL)
		cursor = cursor -> next;
	// when you are at the end, make a node at next
	node* new_node = create(data, NULL);
	cursor -> next = new_node;
}

// function to print entire contents of list 
void print_list(node* current_node) 
{
	// while you're not at end, print, advance to next 
	while(current_node != NULL) {
		printf("%d\n", current_node->data);
		current_node = current_node -> next;
	}
}


// a function to count the size of the list 
int size(node* list)
{
	node* current = list;
	int count = 0;
	// while not at the end, advance, count 
	while(current != NULL) {
		count++;
		current = current -> next;
	}
	return count;
}

// a function to remove the first instance of the target
void nuke(node* list, int target)
{
	node* current = list;
	node* prev    = NULL;

	// if you're already looking at the target, pass 
	// your "next" to the "prev" holder and destroy current
	if(current == NULL && current -> data == target) {
		prev = current -> next;
		free(current);
	}

	// if you aren't, advance, storing the next you were
	// just at to replace you're "next" when you find target
	while(current != NULL && current -> data != target) {
		// hand off location to "previous", advance to next
		prev = current;		current = current -> next;
	}

	// if you never find it, return nothing
	if(prev == NULL) return;

	// make the final handoff - the previous node now points 
	// to the next node after where we will delete the target
	prev -> next = current -> next;

	// delete the memory of target
	free(current);
}

/*------------------------------------------------------------*\
	the main function creates a node, adds to it, and
	then removes the first element and another element
	to make sure the logic for both is working, then
	displays the list to show that it works. 
\*------------------------------------------------------------*/
		

int main()
{

	// create the first node - holds zero, points nowhere
	node* list = create(0, NULL);
	// add "1" to it 
	append(list, 1);

	// from 2-10 add numbers to the list
	for( int i = 2; i < 10; i++ ) {
		append(list, i);
	}

	// print out the size, the list itself  
	printf("size of linked list: %d\n", size(list));
	print_list(list);

	// remove 1 and 4 (testing different logic
	nuke(list,1);
	nuke(list,4);

	// display same things to see if the logic worked 	
	printf("size of linked list: %d\n", size(list));
	print_list(list);


return 0;
}
