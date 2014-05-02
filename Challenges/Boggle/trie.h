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

Trie_node *maketrienodeptr();
// Must be called for each use of maketrienode() to free memory
void freetrienodeptr(Trie_node *);

struct trie {
    Trie_node *root;
};

// return an empty trie
Trie maketrie();
// must be called for each use of maketrie() to free memory
void freetrie(Trie *);
void addword(Trie *, const char *);
bool isprefix(const Trie *, const char *);
bool isword(const Trie *, const char *);
