/**
 * Solution to codeeval sum of primes problem:
 * https://www.codeeval.com/open_challenges/4/
 *
 * Print the sum of the first 1000 primes.
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-03
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct list List;
typedef struct node Node;

struct node {
    Node *next;
    Node *prev;
    int data;
};

struct list {
    Node *head;
    Node *tail;
};

// append to end of list
void list_insert(List *, int value);

// test whether number is prime
int test(List *, int);

int main() {
    List primes;
    primes.head = NULL;
    primes.tail = NULL;
    int counter = 0;
    int num = 2;
    long total = 0;

    while (counter < 1000) {
        if (test(&primes, num)) {
            total += num;
            list_insert(&primes, num++);
            ++counter;
        } else {
            ++num;
        }
    }

    printf("%ld\n", total);
    return 0;
}

void list_insert(List *list, int value) {
    Node *nodeptr = malloc(sizeof(Node));
    nodeptr->data = value;

    if (list->head == NULL) {
        nodeptr->next = NULL;
        nodeptr->prev = NULL;
        list->head = nodeptr;
        list->tail = nodeptr; 
    } else {
        list->tail->next = nodeptr;
        nodeptr->prev = list->tail;
        list->tail = nodeptr;
    }
}

int test(List *primes, int num) {
    Node *it = primes->head;
    int val;

    while (it != NULL) {
        val = it->data;
        if (num % val == 0) return 0;
        if (val * val > num) break;
        it = it->next;
    }
    return 1;
}
