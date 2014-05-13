/**
 * Reverse words challenge from codeeval
 * https://www.codeeval.com/open_challenges/8/
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-12
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define WORDBUFSIZE 128

typedef struct list_node List_node;
typedef struct list List;

struct list_node {
    List_node *next;
    char *word;
};

struct list {
    List_node *head;
};

// initialize an empty list
List *list_make();
// push a string onto the front of the list
void list_push(List *, char *);
// pop a string from front of list
char *list_pop(List *);
// allocate memory for a copy and push to list
void pushcopy(List *, const char *, int);
// print list to stdout
void printlist(List *);

enum { SAMEWORD, NEWWORD };

int main() {
    char c,
        wordbuf[WORDBUFSIZE];
    int state = SAMEWORD,
        bufidx = 0;
    List *mylist = list_make();

    while ((c = getchar()) != EOF) {
        assert(bufidx < WORDBUFSIZE - 1); 
        if (c == '\n') {
            if (bufidx > 0) {
                wordbuf[bufidx++] = '\0';
                pushcopy(mylist, wordbuf, bufidx);
            }
            printlist(mylist);
            bufidx = 0;
            state = NEWWORD;
            continue;
        }
        if (state == SAMEWORD) {
            if (c <= ' ') {
                if (bufidx > 0) {
                    wordbuf[bufidx++] = '\0';
                    pushcopy(mylist, wordbuf, bufidx);
                }
                bufidx = 0;
                state = NEWWORD;
            } else {
                wordbuf[bufidx++] = c;
            }
            continue;
        }
        if (state == NEWWORD) {
            if (c > ' ') {
                state = SAMEWORD;
                wordbuf[bufidx++] = c;
            }
        }
    }

    return 0;
}

List *list_make() {
    List *result = malloc(sizeof(List));

    result->head = NULL;
    return result;
}

void list_push(List *mylist, char *word) {
    List_node *node = malloc(sizeof(List_node));

    node->word = word;
    node->next = mylist->head;
    mylist->head = node;
}

char *list_pop(List *mylist) {
    List_node *oldhead = mylist->head;
    // case of empty list
    if (!oldhead) { return NULL; }

    char *ret = oldhead->word;
    mylist->head = oldhead->next;
    free(oldhead);

    return ret;
}

void pushcopy(List *mylist, const char *word, int size) {
    char *wordcpy = malloc((size + 1) * sizeof(char));

    strcpy(wordcpy, word);
    list_push(mylist, wordcpy);
}

void printlist(List *mylist) {
    int first = 1;

    while (mylist->head != NULL) {
        printf("%s%s", first ? "" : " ", list_pop(mylist));
        first = 0;
    }
    puts("");
}
