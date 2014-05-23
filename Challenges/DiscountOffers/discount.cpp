/**
 * Discount offers challenge from codeeval (hard)
 * https://www.codeeval.com/open_challenges/48/
 *
 * Hungarian algorithm:
 * http://en.wikipedia.org/wiki/Hungarian_algorithm
 *
 * The following doesn't work either, because CLRS doesn't
 * consider edge weights here but only cardinality of the 
 * matching (trivial for our problem).
 * This is a maximum bipartite matching problem.
 * Cf. CLRS, pp. 732ff.
 *
 * Old algorithm:
 * Get a 2D matrix of suitability scores.
 * Transpose it if necessary to make sure that rows >= cols
 * Swap rows to improve the sum along the top diagonal
 * Stop when no more improvement is possible and use that sum.
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
//#include <sstream>
//#include <vector>

int count_vowels(const std::string &);
int count_consonants(const std::string &);
int count_letters(const std::string &);
bool is_vowel(const char &); 
bool is_consonant(const char &); 
bool is_letter(const char &);
bool is_in(const char &, const char *);
double suitability_score(const std::string &, const std::string &);
int ss_int(const std::string &, const std::string &);
double ss_int_to_dbl(const int &); 
bool relative_primes(const unsigned int &, const unsigned int &);
unsigned int gcd(const unsigned int, const unsigned int);
unsigned int gcd_internal(const unsigned int &, const unsigned int &);
int get_row(const int &, const int &);
int get_col(const int &, const int &);
int get_index(const int &, const int &, const int &);
void ss_ints(int *, const std::string *, const size_t &, const std::string *, const size_t &);
void init_residual_graph(int *, const int *, const size_t &, const size_t &);
double max_match(const double *, const size_t &, const size_t &);
// retrieve maximum from an array excluding one index
// values are assumed to be non-negative
double max_excluding(const double *, const size_t &, const int &);
/*
std::vector<std::vector<double> > suitability_scores(const std::vector<std::string> &, 
    const std::vector<std::string> &);
*/
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
    size_t num_customers = 3;
    size_t num_products = 3;
    int *scores;
    int *residual_graph;
    size_t vertices;

    while (std::getline(std::cin, line)) {
        std::cout << count_vowels(line) << std::endl;
        std::cout << count_consonants(line) << std::endl;
        std::cout << count_letters(line) << std::endl;
    }

    scores = new int[num_customers * num_products];
    vertices = num_customers + num_products + 2;
    residual_graph = new int[vertices * vertices];
    // convert products to lowercase
    for (std::string &product : products) {
        std::transform(product.begin(), product.end(), product.begin(), tolower);
    }
    // convert customers to lowercase
    for (std::string &customer : customers) {
        std::transform(customer.begin(), customer.end(), customer.begin(), tolower);
    }

    for (std::string &product : products) {
        for (std::string &customer : customers) {
            std::cout << "\"" << product << "\", \"" << customer << "\": " << 
                suitability_score(product, customer) << std::endl;
        }
    }

    ss_ints(scores, products, num_products, customers, num_customers);
    for (int i = 0; i < num_customers * num_products; ++i) {
        std::cout << scores[i] << std::endl;
    }

    init_residual_graph(residual_graph, scores, num_products, num_customers);
    for (int i = 0; i < vertices; ++i) {
        for (int j = 0; j < vertices; ++j) {
            std::cout << residual_graph[get_index(vertices, i, j)] << " ";
        }
        std::cout << std::endl;
    }

    delete[] residual_graph;
    delete[] scores;

    return 0;
}

int count_vowels(const std::string &input) {
    return std::count_if(input.begin(), input.end(), is_vowel);
}

int count_consonants(const std::string &input) {
    return std::count_if(input.begin(), input.end(), is_consonant);
}

int count_letters(const std::string &input) {
    return std::count_if(input.begin(), input.end(), is_letter);
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

bool is_letter(const char &c) {
    return 'a' <= c && c <= 'z';
}

int ss_int(const std::string &product, const std::string &customer) {
    int prod_ltr_ct = count_letters(product),
        cust_ltr_ct = count_letters(customer);
    int multiple = relative_primes(prod_ltr_ct, cust_ltr_ct) ? 2 : 3;
    if (prod_ltr_ct % 2 == 0) {
        return multiple * 3 * count_vowels(customer);
    }
    return multiple * 2 * count_consonants(customer);
}

double ss_int_to_dbl(const int &ss) {
    return ss / 4.0;
}

double suitability_score(const std::string &product, const std::string &customer) {
    return ss_int_to_dbl(ss_int(product, customer));
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
void ss_ints(int *scores, const std::string *products, const size_t &prod_len, const std::string *customers, const size_t &cust_len) {
    int i, j;

    for (i = 0; i < prod_len; ++i) {
        for (j = 0; j < cust_len; ++j) {
            scores[cust_len * i + j] = ss_int(products[i], customers[j]);
        }
    }
}

// source has index 'end - 2', sink has index 'end - 1'
void init_residual_graph(int *graph, const int *scores, const size_t &rows, const size_t &cols) {
    int max_capacity = *std::max_element(scores, scores + rows * cols);
    size_t vertices = rows + cols + 2;
    int i, j;
    
    // edges from products
    for (i = 0; i < rows; ++i) {
        // to products
        for (j = 0; j < rows; ++j) {
            graph[get_index(vertices, i, j)] = 0;
        }
        // to customers
        for (; j < rows + cols; ++j) {
            graph[get_index(vertices, i, j)] = scores[get_index(cols, i, j - rows)];
        }
        // to source and sink
        for (; j < vertices; ++j) {
            graph[get_index(vertices, i, j)] = 0;
        }
    }
    // edges from customers
    for (; i < rows + cols; ++i) {
        // to products and customers
        for (j = 0; j < rows + cols; ++j) {
            graph[get_index(vertices, i, j)] = 0;
        }
        // to source
        graph[get_index(vertices, i, j)] = 0;
        // to sink
        ++j;
        graph[get_index(vertices, i, j)] = max_capacity;
    }
    // edges from source
    // to products
    for (j = 0; j < rows; ++j) {
        graph[get_index(vertices, i, j)] = max_capacity;
    }
    // to everywhere else
    for (; j < vertices; ++j) {
        graph[get_index(vertices, i, j)] = 0;
    }
    // edges from sink
    ++i;
    for (j = 0; j < vertices; ++j) {
        graph[get_index(vertices, i, j)] = 0;
    }
}

double max_match(const double *scores, const size_t &rows, const size_t &cols) {
    double match_tbl[rows * cols];
    int i, j;

    // initialize first row to values in scores table
    for (j = 0; j < cols; ++j) {
        match_tbl[j] = scores[j];
    }

    // fill in the rest of the table
    for (i = 1; i < rows; ++i) {
        for (j = 0; j < cols; ++j) {
            match_tbl[get_index(cols, i, j)] = scores[get_index(cols, i, j)] + 
                max_excluding(match_tbl + (i - 1) * cols, cols, j);
        }
    }
    return 0;
}

double max_excluding(const double *values, const size_t &len, const int &exclude_index) {
    double max = 0.0;

    for (int i = 0; i < len; ++i) {
        if (i != exclude_index && values[i] > max) {
            max = values[i];
        }
    }
    return max;
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
