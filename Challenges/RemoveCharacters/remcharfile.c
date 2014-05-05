/**
 * Medium codeeval challenge:
 * https://www.codeeval.com/open_challenges/13/
 *
 * Given as command line argument a filename, read lines from the file
 * to get parameters for removing characters from a string.
 * The string from which characters are to be removed will be on a single
 * line followed by a comma and a space, after which on the same line
 * you will find the characters to be stripped. Example line:
 * how are you, abc // output: how re you
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-04
 */

#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE 1024
#define SCRUB_SIZE 256

// sets all values in array to 0
void clear(char *buf, int size);
void processbuffers(char *outtxtbuf, char *intxtbuf, char *scrub);

enum { GETTING_TEXT, FOUND_COMMA, GETTING_SCRUB, NEWLINE };

int main() {
    char filename[256],
        intxtbuf[BUF_SIZE],
        outtxtbuf[BUF_SIZE],
        scrub[SCRUB_SIZE];
    FILE *fptr;
    int state = GETTING_TEXT,
        intxtbufidx = 0,
        c;

    scanf("%255s", filename);
    if ((fptr = fopen(filename, "r")) == NULL) {
        printf("Can't open file \"%s\"\n", filename);
        exit(EXIT_FAILURE);
    }
    clear(scrub, SCRUB_SIZE);
    while ((c = getc(fptr)) != EOF) {
        if (c == '\n') { state = NEWLINE; }
        switch (state) {
        case GETTING_TEXT:
            if (c == ',') {
                intxtbuf[intxtbufidx] = '\0';
                state = FOUND_COMMA;
            } else {
                intxtbuf[intxtbufidx++] = c;
            }
            break;
        case FOUND_COMMA:
            if (c > ' ') {
                state = GETTING_SCRUB;
                scrub[c] = 1;
            }
            break;
        case GETTING_SCRUB:
            scrub[c] = 1;
            break;
        case NEWLINE:
            // process and reset before starting next line
            if (c > ' ') { 
                processbuffers(outtxtbuf, intxtbuf, scrub);
                state = GETTING_TEXT; 
                intxtbufidx = 0;
                clear(scrub, SCRUB_SIZE);
                intxtbuf[intxtbufidx++] = c;
            }
        }
    }
    fclose(fptr);
    // process last line
    processbuffers(outtxtbuf, intxtbuf, scrub);
    return 0;
}

void clear(char *buf, int size) {
    int i;

    for (i = 0; i < size; ++i) {
        buf[i] = 0;
    }
}


void processbuffers(char *outtxtbuf, char *intxtbuf, char *scrub) {
    int outtxtbufidx = 0,
        intxtbufidx = 0,
        c;

    while ((c = intxtbuf[intxtbufidx++]) != '\0') {
        if (!scrub[c]) {
            outtxtbuf[outtxtbufidx++] = c;
        }
    }
    outtxtbuf[outtxtbufidx] = '\0';
    puts(outtxtbuf);
}
