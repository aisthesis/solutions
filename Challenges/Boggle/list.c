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
Trie_node *trie_makenodeptr() {
    int i;
    Trie_node *node = malloc(sizeof(Trie_node));

    for (i = 0; i < ALPHABET_SIZE; ++i) {
        node->children[i] = NULL;
    }
    node->is_word = false;
    return node;
}

void trie_freenodeptr(Trie_node *trienodeptr) {
    int i;

    for (i = 0; i < ALPHABET_SIZE; ++i) {
        if (trienodeptr->children[i] != NULL) {
            trie_freenodeptr(trienodeptr->children[i]);
        }
    }
    free(trienodeptr);
}

Trie trie_make() {
    Trie trie;

    trie.root = trie_makenodeptr();
    return trie;
}

void trie_free(Trie *trieptr) {
    trie_freenodeptr(trieptr->root);
}

void trie_addword(Trie *trieptr, const char *word) {
    Trie_node *node = trieptr->root,
        *tmp;
    int index;

    while (*word != '\0') {
        index = *word - 'a';
        if (node->children[index] == NULL) {
            tmp = trie_makenodeptr();
            node->children[index] = tmp;
        }
        node = node->children[index];
        word++;
    }
    node->is_word = true;
}

bool trie_isprefix(const Trie *trieptr, const char *prefix) {
    Trie_node *nodeptr = trieptr->root;
    int index;

    while (*prefix != '\0') {
        index = *prefix - 'a';
        if (nodeptr->children[index] == NULL) { return false; }
        nodeptr = nodeptr->children[index];
        prefix++;
    }
    return true;
}

bool trie_isword(const Trie *trieptr, const char *prefix) {
    Trie_node *nodeptr = trieptr->root;
    int index;

    while (*prefix != '\0') {
        index = *prefix - 'a';
        if (nodeptr->children[index] == NULL) { return false; }
        nodeptr = nodeptr->children[index];
        prefix++;
    }
    return nodeptr->is_word;
}
