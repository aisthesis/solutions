/**
 * Trie (prefix tree) datastructure implementation
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-04-29
 */

#include <stdio.h>
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
Trienode maketrienode(bool is_word) {
    int i;
    Trienode node;

    for (i = 0; i < ALPHABET_SIZE; ++i) {
        node.children[i] = NULL;
    }
    node.is_word = is_word;
    return node;
}
