/**
 * Trie (prefix tree) datastructure implementation
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-04-29
 */

#include <stdio.h>
#include <stdlib.h>
#include "trie.h"

/**
 * Note that for integral data types in sequence, such as lowercase
 * letters, we don't need to include the value, which can be deduced
 * immediately from the position of the node in the `children' array
 * of the parent node.
 *
 * Specifically, t.children[0] points to the node for the character 'a',
 * t.children[1] points to the node for 'b', etc. And if no prefix continues
 * with 'a', then t.children[0] points to NULL.
 */
Trienode *maketrienodeptr() {
    int i;
    Trienode *node = malloc(sizeof(Trienode));

    for (i = 0; i < ALPHABET_SIZE; ++i) {
        node->children[i] = NULL;
    }
    node->is_word = false;
    return node;
}

void freetrienodeptr(Trienode *trienodeptr) {
    int i;

    for (i = 0; i < ALPHABET_SIZE; ++i) {
        if (trienodeptr->children[i] != NULL) {
            freetrienodeptr(trienodeptr->children[i]);
        }
    }
    free(trienodeptr);
}

Trie maketrie() {
    Trie trie;

    trie.root = maketrienodeptr();
    return trie;
}

void freetrie(Trie *trieptr) {
    freetrienodeptr(trieptr->root);
}

void addword(Trie *trieptr, const char *word) {
    Trienode *node = trieptr->root,
        *tmp;
    int index;

    while (*word != '\0') {
        index = *word - 'a';
        if (node->children[index] == NULL) {
            tmp = maketrienodeptr();
            node->children[index] = tmp;
        }
        node = node->children[index];
        word++;
    }
    node->is_word = true;
}

bool isprefix(const Trie *trieptr, const char *prefix) {
    Trienode *nodeptr = trieptr->root;
    int index;

    while (*prefix != '\0') {
        index = *prefix - 'a';
        if (nodeptr->children[index] == NULL) { return false; }
        nodeptr = nodeptr->children[index];
        prefix++;
    }
    return true;
}

bool isword(const Trie *trieptr, const char *prefix) {
    Trienode *nodeptr = trieptr->root;
    int index;

    while (*prefix != '\0') {
        index = *prefix - 'a';
        if (nodeptr->children[index] == NULL) { return false; }
        nodeptr = nodeptr->children[index];
        prefix++;
    }
    return nodeptr->is_word;
}
