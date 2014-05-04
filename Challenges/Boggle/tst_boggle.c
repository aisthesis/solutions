/**
 * Tests for boggle-solver.
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-02
 */

#include <stdio.h>
#include <stdlib.h>
#include "trie.h"
#include "list.h"
#include "boggle.h"

#define PUZZLE_ROWS 5
#define PUZZLE_COLS 6

int main() {
    char *findablewords[] = { "be", "bid", "cat", "do", "dog", "dogs", "god", "mouse", "cite", "bet", "alphabet" };
    size_t num_findable = 11;
    char *unfindablewords[] = { "zoo", "alphabetical", "better" };
    size_t num_unfindable = 3;
    size_t rows = 5;
    size_t cols = 6;
    size_t len = rows * cols;
    char puzzle[] = {
        'c', 'a', 't', 'b', 'e', 't',
        'a', 'd', 'a', 'a', 'l', 'i',
        'm', 'o', 'u', 'h', 'p', 'c',
        'a', 'g', 's', 'a', 'l', 'a',
        'a', 'a', 'e', 'b', 'i', 'd'};
    Trie dictionary = trie_make();
    List answer[len];
    int i, found = 0;
    List_node *listnodeptr;

    // insert words into dictionary
    for (i = 0; i < num_findable; ++i) {
        trie_addword(&dictionary, findablewords[i]);
    }
    for (i = 0; i < num_unfindable; ++i) {
        trie_addword(&dictionary, unfindablewords[i]);
    }

    // create parallel array of empty lists
    for (i = 0; i < len; ++i) {
         answer[i] = list_make();
    }

    // pass given parameters to boggle solver
    boggle_solve(answer, puzzle, PUZZLE_ROWS, PUZZLE_COLS, &dictionary);
    for (i = 0; i < len; ++i) {
        if (answer[i].head != NULL) {
            printf("row %lu, col %lu:\n", i / cols, i % cols);
            listnodeptr = answer[i].head;
            while (listnodeptr != NULL) {
                ++found;
                printf("\t%s\n", listnodeptr->data);
                listnodeptr = listnodeptr->next;
            }
        }
    }
    printf("%d word%s found.\n", found, found == 1 ? "" : "s");
    return 0;
}
