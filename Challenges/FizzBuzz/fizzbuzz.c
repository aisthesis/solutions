/**
 * Simple codeeval challenge:
 * https://www.codeeval.com/open_challenges/1/
 *
 * Take 3 numbers A, B and N from stdin on each line and output a "fizz/buzz"
 * game accordingly.
 * The output is counting up to N unless the number is divisible by A or B.
 * If divisible by A, output 'F'. If divisible by B output 'B'. If divisible
 * by both, output 'FB'.
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-03
 */

#include <stdio.h>

void fizzbuzz(long a, long b, long n);

int main() {
    long a, b, n;

    while (scanf("%ld %ld %ld", &a, &b, &n) != EOF) {
        fizzbuzz(a, b, n);
    }
    return 0;
}

void fizzbuzz(long a, long b, long n) {
    int first = 1; 
    long i;

    for (i = 1L; i <= n; ++i) {
        if (i % a == 0) {
            if (i % b == 0) {
                printf("%sFB", first ? "" : " ");
            } else {
                printf("%sF", first ? "" : " ");
            }
        } else if (i % b == 0) {
            printf("%sB", first ? "" : " ");
        } else {
            printf("%s%ld", first ? "" : " ", i);
        }
        if (first) first = 0;
    }
    puts("");
    puts("test");
}
