/**
 * Solves a boggle puzzle with the specified
 * number of rows and columns. Characters are
 * presumed to be lower case, and the answer is provided
 * as a 2-dimensional array of lists, where each
 * entry is the list of words found starting from 
 * the given position--or NULL if no word is found.
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-03
 */

#ifndef BOGGLE_H
#define BOGGLE_H

#include <stddef.h>
#include "list.h"
#include "trie.h"

// insert the solution to the puzzle into the answer array, which is assumed to be
// an array of empty lists
void boggle_solve(List *answer, const char *puzzle, size_t rows, size_t cols, Trie *dictionary);

#endif
