/**
 * Convert hex to decimal
 * https://www.codeeval.com/open_challenges/67/
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-19
 */

#include <iostream>
#include <string>

int hex_to_int(const std::string &);

int main() {
    std::string line;

    while (std::getline(std::cin, line)) {
        std::cout << hex_to_int(line) << std::endl;
    }
    return 0;
}

int hex_to_int(const std::string &line) {
    int total = 0;
    const int base = 16;

    for (const char &c : line) {
        total *= base;
        if (c < 'a') {
            total += c - '0';
        } else {
            total += c - 'a' + 10;
        }
    }
    return total;
}
