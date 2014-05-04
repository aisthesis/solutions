/**
 * Doubly linked list.
 * Nodes can carry any data type, as they are pointers
 * to type void.
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-02
 */

#ifndef LIST_H
#define LIST_H

typedef struct list_node List_node;
typedef struct list List;

struct list_node {
    void *data;
    List_node *prev;
    List_node *next;  
};

struct list {
    List_node *head;
    List_node *tail;
};

// make an empty list
List list_make();
// free up memory used by a list that isn't needed
void list_free(List *);
// insert an item at the head of the list
void list_push(List *, void *);
// remove and return the item at the head of the list
void *list_pop(List *);

#endif
