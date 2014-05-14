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

#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <list>

void init_found(bool *, const size_t &);
void show_cycle(const std::string &, bool *, const size_t &);
void show_from_val(std::list<int> &, const int &);

int main() {
    const size_t range_size = 100;
    bool found[range_size];
    std::string line;

    while (std::getline(std::cin, line)) {
        init_found(found, range_size);
        show_cycle(line, found, range_size);
    }

    return 0;
}

void init_found(bool *found, const size_t &size) {
    for (size_t i = 0; i < size; ++i) {
        found[i] = false;
    }
}

void show_cycle(const std::string &line, bool *found, const size_t &found_size) {
    std::istringstream iss(line);
    std::istream_iterator<int> it(iss),
        eos;
    std::list<int> numbers;

    while (it != eos) {
        if (found[*it]) {
            show_from_val(numbers, *it);
            return;
        }
        numbers.push_back(*it);
        found[*it++] = true;
    }
}

void show_from_val(std::list<int> &numbers, const int &val) {
    bool show = false;

    while (!numbers.empty()) {
        if (show) {
            std::cout << " " << numbers.front();
        }
        else if (numbers.front() == val) { 
            show = true;
            std::cout << val;
        }
        numbers.pop_front();
    }
    std::cout << std::endl;
}
