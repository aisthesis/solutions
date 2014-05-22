/**
 * Discount offers challenge from codeeval (hard)
 * https://www.codeeval.com/open_challenges/48/
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-22
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>

int count_vowels(const std::string &);
int count_consonants(const std::string &);
bool is_vowel(const char &); 
bool is_consonant(const char &); 
bool is_in(const char &, const char *);
double suitability_score(const std::string &, const std::string &);
bool relative_primes(const unsigned int &, const unsigned int &);
unsigned int gcd(const unsigned int, const unsigned int);
unsigned int gcd_internal(const unsigned int &, const unsigned int &);
int get_row(const int &, const int &);
int get_col(const int &, const int &);
int get_index(const int &, const int &, const int &);
double *suitability_scores(const std::string *, const size_t &, const std::string *, const size_t &);
std::vector<std::vector<double> > suitability_scores(const std::vector<std::string> &, 
    const std::vector<std::string> &);

int main() {
    std::string line;
    //std::istringstream iss;
    //unsigned int test_cases[] = { 1, 5, 10, 21, 70, 91, 1232345 };
    std::string customers[] = {
        "Jack Abraham",
        "John Evans",
        "Ted Dziuba"
    };
    std::string products[] = {
        "iPad 2 - 4-pack",
        "Girl Scouts Thin Mints",
        "Nerf Crossbow"
    };

    while (std::getline(std::cin, line)) {
        std::cout << count_vowels(line) << std::endl;
        std::cout << count_consonants(line) << std::endl;
        std::cout << 1.5 * 9 << std::endl;
    }

    for (std::string &product : products) {
        for (std::string &customer : customers) {
            std::cout << "\"" << product << "\", \"" << customer << "\": " << 
                suitability_score(product, customer) << std::endl;
        }
    }
/*
    for (unsigned int val1 : test_cases) {
        for (unsigned int val2 : test_cases) {
            std::cout << "gcd(" << val1 << ", " << val2 << "): " << gcd(val1, val2) << std::endl;
        }
    }
*/
    return 0;
}

int count_vowels(const std::string &input) {
    return std::count_if(input.begin(), input.end(), is_vowel);
}

int count_consonants(const std::string &input) {
    return std::count_if(input.begin(), input.end(), is_consonant);
}

bool is_in(const char &c, const char *char_list) {
    while (*char_list != '\0') {
        if (c == *char_list++) { return true; }
    }
    return false;
}

bool is_vowel(const char &c) {
    return is_in(c, "aeiou");
}

bool is_consonant(const char &c) {
    return is_in(c, "bcdfghjklmnpqrstvwxyz");
}

double suitability_score(const std::string &product, const std::string &customer) {
    double multiple = relative_primes(product.size(), customer.size()) ? 1.0 : 1.5;
    if (product.size() % 2 == 0) {
        return multiple * 1.5 * count_vowels(customer);
    }
    return multiple * count_consonants(customer);
}

bool relative_primes(const unsigned int &a, const unsigned int &b) {
    return gcd(a, b) == 1;
}

unsigned int gcd(const unsigned int a, const unsigned int b) {
    if (a <= b) { return gcd_internal(a, b); }
    return gcd_internal(b, a);
}

unsigned int gcd_internal(const unsigned int &smaller, const unsigned int &larger) {
    if (larger % smaller == 0) { return smaller; }
    return gcd_internal(larger % smaller, smaller);
}

// products will be rows, customers columns
std::vector<std::vector<double> > suitability_scores(const std::vector<std::string> &products, 
    const std::vector<std::string> &customers) {
    int rows = products.size(),
        cols = customers.size(),
        i, j;

    std::vector<std::vector<double> > scores(rows);
    /*
    for (i = 0; i < rows; ++i) {
        scores[i] = 
    }
    */
    return scores;
}

int get_row(const int &cols, const int &index) {
    return index / cols;
}

int get_col(const int &cols, const int &index) {
    return index % cols;
}

int get_index(const int &cols, const int &row, const int &col) {
    return row * cols + col;
}
