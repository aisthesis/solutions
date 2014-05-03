/**
 * Tests for list.
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-02
 */

#include <stdio.h>
#include <stdlib.h>
#include "list.h"

int main() {
    char *words[] = { "cat", "dog", "mouse", "alphabetical" };
    char *word;
    int num_words = 4;
    List list = list_make();
    int i;

    for (i = 0; i < num_words; ++i) {
        list_push(&list, words[i]);
    }
    while (list.head != NULL) {
        puts(list_pop(&list));
    }
    for (i = 0; i < num_words; ++i) {
        list_push(&list, words[i]);
    }
    list_free(&list);
    if ((word = list_pop(&list))) { 
        printf("%s remains!\n", word);
    } else {
        puts("list destroyed");
    }
    return 0;
}
