/**
 * Trie (prefix tree) header file.
 * This trie will hold only lowercase letters.
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-04-29
 */

#include <stdbool.h>

#define ALPHABET_SIZE 26

typedef struct trie_node Trie_node;
typedef struct trie Trie;

struct trie_node {
    Trie_node *children[ALPHABET_SIZE];
    bool is_word;
};

Trie_node *trie_makenodeptr();
// Must be called for each use of maketrienode() to free memory
void trie_freenodeptr(Trie_node *);

struct trie {
    Trie_node *root;
};

// return an empty trie
Trie trie_make();
// must be called for each use of trie_make() to free memory
void trie_free(Trie *);
void trie_addword(Trie *, const char *);
bool trie_isprefix(const Trie *, const char *);
bool trie_isword(const Trie *, const char *);
