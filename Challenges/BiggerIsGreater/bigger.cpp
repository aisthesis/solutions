/**
 * Bigger is Greater challenge from hackerrank
 * https://www.hackerrank.com/challenges/bigger-is-greater
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2015-04-30
 */

#include <algorithm>
#include <cstring>
#include <iostream>

constexpr std::size_t BUFSIZE = 101;


void increment_selected(char *start, char *last); 
void make_bigger(char *buffer); 
void swap_bigger(char *start, char *last);
void swap(char *a, char *b);

int main() {
    char buffer[BUFSIZE];
    int t;

    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        std::cin >> buffer;
        make_bigger(buffer);
        std::cout << buffer << std::endl;
    }
    return 0;
}

void increment_selected(char *start, char *last) {
    swap_bigger(start, last);
    // reverse the sorting order after start
    ++last;
    while (++start < --last) {
        swap(start, last);
    }
}

void make_bigger(char *buffer) {
    char *last = std::find(buffer, buffer + BUFSIZE, '\0') - 1;
    char *runner = last;
    while (--runner >= buffer) {
        if (*runner < *(runner + 1)) {
            increment_selected(runner, last);
            return;
        }
    }
    if (runner < buffer) {
        std::strcpy(buffer, "no answer");
    }
}

void swap_bigger(char *start, char *last) {
    char *to_swap = start;
    while (++to_swap <= last) {
        if (*to_swap <= *start) {
            break;
        }
    }
    swap(start, --to_swap);
}

void swap(char *a, char *b) {
    char tmp = *a;
    *a = *b;
    *b = tmp;
}
