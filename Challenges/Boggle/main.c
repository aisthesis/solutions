/**
 * Executable boggle solver
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-04-29
 */

#include <stdio.h>
#include <stdbool.h>
#include "trie.h"

int main() {
    int i;
    Trienode t = maketrienode(false);

    if (t.is_word) {
        printf("Prefix forms a complete word.\n");
    } else {
        printf("Prefix does not form a complete word.\n");
    }
    return 0;
}
