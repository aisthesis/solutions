/**
 * Tests for trie.
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-04-29
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "trie.h"

void test_prefix(Trie *, char *);
void test_word(Trie *, char *);

int main() {
    char *word = "cat",
        *emptystr = "",
        *goodprefix = "ca",
        *badprefix = "do";
    Trie trie = trie_make();

    trie_addword(&trie, word);
    test_prefix(&trie, goodprefix);
    test_prefix(&trie, badprefix);
    test_word(&trie, word);

    puts("Before adding empty string to trie:");
    test_prefix(&trie, emptystr);
    test_word(&trie, emptystr);
    trie_addword(&trie, emptystr);
    puts("After adding empty string to trie:");
    test_prefix(&trie, emptystr);
    test_word(&trie, emptystr);

    trie_free(&trie);
    return 0;
}

void test_prefix(Trie *trie, char *prefix) {
    if (trie_isprefix(trie, prefix)) {
        printf("\"%s\" is a prefix.\n", prefix);
    } else {
        printf("\"%s\" is not a prefix.\n", prefix);
    }
}

void test_word(Trie *trie, char *word) {
    if (trie_isword(trie, word)) {
        printf("\"%s\" is a word.\n", word);
    } else {
        printf("\"%s\" is not a word.\n", word);
    }
}
