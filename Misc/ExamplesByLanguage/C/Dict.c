/*** a program to create dict-like behavior in C ***/

#include <stdio.h>
#include <stdlib.h>

/* forward declarations - details after main() */
struct Node *createNode(char *key, char *value, struct Node *next);
void appendList(struct Node *head, char *key, char *value);
void printDict(struct Node *currentNode);
char *lookUp(char *value, struct Node *d);
int listSize(struct Node *head);
void deleteEntry(char *entry, struct Node **head);
void deleteList(struct Node **headRef);

/* structs */
// as linked list ut with key/value pairs
struct Node {
    char *key;
    char *value;
    struct Node *next;
};


int main()
{
    // create a head to serve as dict
    struct Node *dictHead = createNode("Thadryan", "Sweeney", NULL);

    // append two entries
    appendList(dictHead, "Kyle", "Sargent");
    appendList(dictHead, "Bethany", "Johnson");
    printDict(dictHead);

    // should be 3
    printf("length of dict: %d\n", listSize(dictHead));

    deleteEntry("Thadryan", &dictHead);
    printDict(dictHead);
    // should be 2
    printf("length of dict: %d\n", listSize(dictHead));

    // use lookUp
    printf("The value for key \"Bethany\" is %s\n", lookUp("Bethany", dictHead));
    // should warn
    printf("The value for key \"Thadryan\" is %s\n", lookUp("Thadryan", dictHead));

    deleteList(&dictHead);

    // should be empty
    printDict(dictHead);

}


/* function definitions */

// make a new node - basically an ll function
struct Node *createNode(char *key, char *value, struct Node *next)
{
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = next;
    return newNode;
};

// add an entry to the end of Dict
void appendList(struct Node *head, char *key, char *value)
{
    struct Node *cursor = head;
    // while there is still a node to go
    while(cursor->next != NULL)
        cursor = cursor->next;
    // stop and make a new node at the end
    struct Node *new_node = createNode(key, value, NULL);
    // set new node
    cursor->next = new_node;
};

// prints entire list of k,v pairs
void printDict(struct Node *currentNode)
{
    if(currentNode == NULL)
        printf("The list is empty\n");
    while(currentNode != NULL) {
        printf("key: %s, value: %s\n", currentNode->key, currentNode->value);
        currentNode = currentNode->next;
    }
}

// gets number of PAIRS
int listSize(struct Node *head)
{
    // count while not NULL
    struct Node *current = head;
    int count = 0;
    while(current != NULL) {
        count++;
        current = current->next;
    }
    return count;
}

// takes key, brings value
char *lookUp(char *value, struct Node *d)
{
  // default answer
  char *current = "KEYNOTFOUND";
	char *result = current;
    while(d != NULL) {
        if(d->key == value)
            result = d->value;
        d = d->next;
	}
  // if we are still on default
	if(result == current)
		printf("Warning: no result found for %s, returning default\n", value);
	return result;
}

// deletes whole list
void deleteList(struct Node **headRef)
{
    struct Node *current = *headRef;
    struct Node *next;

    while(current != NULL) {
        // move up, delete your tracks
        next = current->next;
        free(current);
        current = next;
    }
    // delete the head
    *headRef = NULL;
}

// deletes first occurence of specific entries
void deleteEntry(char *key, struct Node **headRef)
{
    struct Node *temp = *headRef, *previous;
    // if we are starting on it, move head up, delete "current"
    if(temp != NULL && temp->key == key) {
        *headRef = temp->next; // why you need a ref
        free(temp);
        return;
    }
    // if we haven't found the key or the end
    while(temp != NULL && temp->key != key) {
        previous = temp;
        temp = temp->next;
    }
    // if we never found it, bail
    if(previous == NULL) return;

    // or else previous becomes new head, delete old head
    previous->next = temp->next;
    free(temp);
}
