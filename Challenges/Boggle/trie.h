/**
 * Trie (prefix tree) header file
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-04-29
 */

#include <stdbool.h>

#define ALPHABET_SIZE 26

typedef struct trienode Trienode;

struct trienode {
    Trienode *children[ALPHABET_SIZE];
    unsigned char value;
    bool is_word;
};

Trienode maketrienode(bool is_word);
