/**
 * Linked list implementation.
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-02
 */

#include <stdlib.h>
#include "list.h"

List list_make() {
    List list;
    list.head = NULL;
    list.tail = NULL;
    return list;
}

void list_free(List *listptr) {
    List_node *nodeptr1 = listptr->head, 
        *nodeptr2;

    while (nodeptr1 != NULL) {
        nodeptr2 = nodeptr1->next;
        free(nodeptr1);
        nodeptr1 = nodeptr2;
    }
    listptr->head = NULL;
    listptr->tail = NULL;
}

void list_push(List *list, void *data) {
    List_node *nodeptr = malloc(sizeof(List_node));
    nodeptr->data = data;
    nodeptr->next = list->head;
    nodeptr->prev = NULL;
    if (list->head == NULL) {
        list->tail = nodeptr;
    } 
    list->head = nodeptr;
}

void *list_pop(List *list) {
    List_node *oldhead = list->head;
    // if the list is empty
    if (oldhead == NULL) return NULL;

    list->head = oldhead->next;
    if (list->head == NULL) {
        list->tail = NULL;
    } else {
        list->head->prev = NULL;
    }
    void *data = oldhead->data;
    free(oldhead);
    return data;
}
