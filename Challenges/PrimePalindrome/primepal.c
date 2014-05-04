/**
 * Solution to codeeval prime palindrome problem:
 * https://www.codeeval.com/open_challenges/3/
 *
 * Print the larges prime palindrome under 1000.
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-03
 */

#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

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

unsigned int decimaldigits(unsigned int);
unsigned int isintpalindrome(unsigned int);
unsigned int isarrpalindrome(unsigned int *, size_t);

int main() {
    List primes;
    primes.head = NULL;
    primes.tail = NULL;
    unsigned int num = 2;
    unsigned int answer = 2;

    while (num < MAX) {
        if (test(&primes, num)) {
            list_insert(&primes, num);
            if (isintpalindrome(num)) {
                answer = num;
            }
        } 
        ++num;
    }
    printf("%d\n", answer);
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

unsigned int decimaldigits(unsigned int num) {
    unsigned int result = 1;
    while ((num = num / 10)) { ++result; }
    return result;
}

unsigned int isintpalindrome(unsigned int num) {
    size_t size = decimaldigits(num);
    unsigned int *arr = malloc(size * sizeof(unsigned int));
    size_t i = size - 1;
    do {
        arr[i--] = num % 10;
        num /= 10;
    } while (num > 0);
    int answer = isarrpalindrome(arr, size);
    free(arr);
    return answer;
}
unsigned int isarrpalindrome(unsigned int *arr, size_t size) {
    size_t i = 0,
        j = size - 1;
    while (i < j) {
        if (arr[i++] != arr[j--]) { return 0; }
    }
    return 1;
}
