/**
 * Template from Skiena et al., Programming Challenges, p. 8
 * for standard input/output
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-03
 */

#include <stdio.h>

int main() {
    long p, q;

    while (scanf("%ld %ld", &p, &q) != EOF) {
        printf("%ld\n", p + q);
    }
    return 0;
}
