/**
 * Solution to codeeval ugly numbers problem (sponsored)
 * https://www.codeeval.com/public_sc/42/
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-11
 */

#include <stdio.h>

#define INBUFFSIZE 14
#define DIGBUFFSIZE 25

enum { NOTHING, PLUS, MINUS };

long long isugly(long long);
void isuglytst();
// return effective length of buffer (relevant positions)
int initdigbuf(char *, const char *);
// return 0 if incrementing is no longer possible
int incrementdigbuf(char *, int);
long long eval(const char *, int);
// count how many ugly numbers can be formed
long long uglycount(char *, int);
// for testing
void show(const char *, int);

int main() {
    char inputbuf[INBUFFSIZE],
        digbuf[DIGBUFFSIZE];
    int digbuflen; 

    while (scanf("%s", inputbuf) != EOF) {
        digbuflen = initdigbuf(digbuf, inputbuf);
        printf("%lld\n", uglycount(digbuf, digbuflen));
    }

    return 0;
}

long long isugly(long long num) {
    int divisors[] = { 2, 3, 5, 7};
    int len = 4;
    int i;

    for (i = 0; i < len; ++i) {
        if (num % divisors[i] == 0) { return 1; }
    }
    
    return 0;
}

void isuglytst() {
    int ugly[] = { -14, -39, 14, 236 };
    int uglylen = 4;
    int notugly[] = { 13, 121, 71 };
    int notuglylen = 3;
    int i;

    // test uglies
    for (i = 0; i < uglylen; ++i) {
        if (isugly(ugly[i])) {
            printf("%d is ugly\n", ugly[i]);
        } else {
            printf("%d is not ugly\n", ugly[i]);
        }
    }

    // test non-uglies
    for (i = 0; i < notuglylen; ++i) {
        if (isugly(notugly[i])) {
            printf("%d is ugly\n", notugly[i]);
        } else {
            printf("%d is not ugly\n", notugly[i]);
        }
    }
}

int initdigbuf(char *digbuf, const char *inputbuf) {
    int digbufindex = 0;

    if (*inputbuf != '\0') {
        digbuf[digbufindex++] = *inputbuf++ - '0';
        while (*inputbuf != '\0') {
            digbuf[digbufindex++] = NOTHING;
            digbuf[digbufindex++] = *inputbuf++ - '0';
        }
    }

    return digbufindex;
}

int incrementdigbuf(char *digbuf, int len) {
    int i = len;
    while ((i -= 2) > 0) {
        if (digbuf[i] < MINUS) {
            ++digbuf[i];
            return 1;
        } else {
            digbuf[i] = NOTHING;
        }
    }
    return 0;
}

long long eval(const char *digbuf, int len) {
    int operation = PLUS,
        max = len - 2,
        i;
    long long stored = 0LL,
        val = 0LL;

    for (i = 0; i < max; i += 2) {
        val += digbuf[i];
        if (digbuf[i + 1] == NOTHING) {
            val *= 10;
        } else {
            if (operation == PLUS) {
                stored += val;
            } else {
                // MINUS
                stored -= val;
            }
            val = 0;
            operation = digbuf[i + 1];
        }
    }
    val += digbuf[i];
    if (operation == PLUS) {
        stored += val;
    } else {
        // MINUS
        stored -= val;
    }
    return stored;
}

long long uglycount(char *digbuf, int len) {
    long long uglies = 0;
    if (isugly(eval(digbuf, len))) { ++uglies; }
    while (incrementdigbuf(digbuf, len)) {
        if (isugly(eval(digbuf, len))) { ++uglies; }
    }
    return uglies;
}

void show(const char *buf, int len) {
    int i;

    puts("Buffer:");
    for (i = 0; i < len; ++i) {
        printf("%d ", buf[i]);
    }
    puts("");
}
