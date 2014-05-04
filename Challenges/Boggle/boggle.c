/**
 * Boggle solver implementation.
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-03
 */

#include <stdlib.h>
#include <string.h>
#include "boggle.h"

#define BUFFER_SIZE 256

enum { BLACK, WHITE };

size_t getrow(size_t index, size_t cols) {
    return index / cols; 
}

size_t getcol(size_t index, size_t cols) {
    return index % cols;
}

size_t getindex(size_t row, size_t col, size_t cols) {
    return row * cols + col;
}

void solveloc(List *answer, const char *puzzle, size_t rows, size_t cols, Trie *dictionary, 
    int *colors, char *prefixbuf, size_t bufidx, size_t puzzlei, size_t puzzlej) {
    // trying to find a string that is too long
    if (bufidx >= BUFFER_SIZE - 1) return;
    // already being explored, so off limits
    int curridx = getindex(puzzlei, puzzlej, cols);
    if (colors[curridx] == BLACK) return;

    prefixbuf[bufidx] = puzzle[curridx];
    prefixbuf[bufidx + 1] = '\0';
    // current attempt is not a prefix, so clean up and move on
    if (!trie_isprefix(dictionary, prefixbuf)) {
        prefixbuf[bufidx] = '\0';
        return;
    }
    char *tmp;
    // add word if found
    if (trie_isword(dictionary, prefixbuf)) {
        tmp = malloc((bufidx + 2) * sizeof(char));
        strcpy(tmp, prefixbuf);
        list_push(answer, tmp);
    }
    // color current node BLACK
    colors[curridx] = BLACK;
    // explore adjacent nodes
    if (puzzlei > 0) {
        // node above
        solveloc(answer, puzzle, rows, cols, dictionary, colors, prefixbuf, bufidx + 1, 
            puzzlei - 1, puzzlej);
    }
    if (puzzlej > 0) {
        // node to the left
        solveloc(answer, puzzle, rows, cols, dictionary, colors, prefixbuf, bufidx + 1, 
            puzzlei, puzzlej - 1);
    }
    if (puzzlej < cols - 1) {
        // node to the right
        solveloc(answer, puzzle, rows, cols, dictionary, colors, prefixbuf, bufidx + 1, 
            puzzlei, puzzlej + 1);
    }
    if (puzzlei < rows - 1) {
        // node below
        solveloc(answer, puzzle, rows, cols, dictionary, colors, prefixbuf, bufidx + 1, 
            puzzlei + 1, puzzlej);
    }
    // clean up current node
    prefixbuf[bufidx] = '\0';
    colors[curridx] = WHITE;
}

void boggle_solve(List *answer, const char *puzzle, size_t rows, size_t cols, Trie *dictionary) {
    //list_push(answer, "cat");
    char prefixbuf[BUFFER_SIZE];
    size_t len = rows * cols;
    int *colors = malloc(len * sizeof(int));
    int i, j;

    // initialize all colors to WHITE
    for (i = 0; i < len; ++i) {
        colors[i] = WHITE;
    }
    prefixbuf[0] = '\0';

    for (i = 0; i < rows; ++i) {
        for (j = 0; j < cols; ++j) {
            solveloc(answer + cols * i + j, puzzle, rows, cols, dictionary, colors, prefixbuf, 0, i, j);
        }
    }
    free(colors);
}
