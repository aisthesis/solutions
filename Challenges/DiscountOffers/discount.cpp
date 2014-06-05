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
#include <vector>
#include <algorithm>
#include <cstdio>

void process_line(const std::string &);
std::vector<std::string> tokenize(const std::string &, const char &);
void set_scores(int *, const int &, const std::vector<std::string> &, const std::vector<std::string> &);
int get_scorei(const std::string &, const std::string &);
int count_vowels(const std::string &);
int count_consonants(const std::string &);
int count_letters(const std::string &);
bool is_vowel(const char &); 
bool is_consonant(const char &); 
bool is_letter(const char &);
bool is_in(const char &, const char *);
bool relative_primes(const unsigned int &, const unsigned int &);
unsigned int gcd(const unsigned int, const unsigned int);
unsigned int gcd_internal(const unsigned int &, const unsigned int &);
double scoreitodbl(const int &); 

class Index {
    private:
    // the number of columns
    int cols_;

    public:
    Index(const int &);
    ~Index() {};

    int row(const int &) const;
    int col(const int &) const;
    int index(const int &, const int &) const;
};

class MaxMatch {
private:
    const int rows_;
    const int cols_;
    const Index index_;
    int *graph_,
        *match_by_X_,
        *match_by_Y_,
        *childX_;
public:
    MaxMatch(const int *, const int &, const int &);
    ~MaxMatch();
    // run the algorithm to get the matching
    void init();
    /**
     * get the Y element matching a given X element.
     * return -1 if no element matches
     */
    int match_X(const int &) const;
    /**
     * get the X element matching a given Y element
     * return -1 if no element matches
     */
    int match_Y(const int &) const;
    /**
     * return the number of matches found
     */
    int matches() const;
    /**
     * reset the graph on which to find a matching.
     * presupposes the same number of rows and
     * columns.
     * Also resets match_by_row_ and match_by_col_ to 0s
     */
    void set(const int *);
    /**
     * Does not reset matchings to avoid unnecessary repetition
     */
    void add_graph_edge(const int &, const int &);
    void delete_graph_edge(const int &, const int &);
    bool has_graph_edge(const int &, const int &);
    int sizeX() const;
    int sizeY() const;
    void reset();
private:
    void reset_matches();
    void reset_childX();
    /**
     * Return the start of an augmenting path, if there
     * is one. Otherwise, return -1.
     */
    int dfs();
    /**
     * recursive search starting at a given X vertex.
     */
    bool dfs_visit(const int &);
    void augment_match(int);
};

class Hungarian {
private:
    // the number of rows (or cols, since matrix is square)
    const int len_;
    const int len_sq_;
    /**
     * the graph is bipartite, but edges may have weight 0
     * to deal with the case where the sets to match have different
     * sizes
     */
    int *weights_;
    /**
     * edges will just be 0 or 1.
     * Edges in this graph may be 1 for 0 weight edges (to
     * padded vertices) in main graph
     */
    int *equality_graph_;
    int *labelsX_;
    int *labelsY_;
    // 1 for members of S, 0 for non-members
    int *S_;
    // 1 for members of T, 0 for non-members
    int *T_;
    // 1 for members of NlS, 0 for non-members
    int *NlS_;
    Index index_;
    MaxMatch matcher_;

public:
    Hungarian(const int *weights, const int &len);
    ~Hungarian();

    int get_match_total();
    int matchX(const int &) const;
    int matchY(const int &) const;
    int length() const;
    int weight(const int &, const int &) const;
    void init();

private:
    void improve_equality_graph();
    int get_free_vertex() const;
    void update_equality_graph();
    int get_alpha() const;
    // S_, T_, NlS_
    void reset_path_sets();
    void update_NlS(const int &);
    int nls_minus_t() const;
    void relabel();
};

int main() {
    std::string line;

    while (std::getline(std::cin, line)) {
        std::transform(line.begin(), line.end(), line.begin(), tolower);
        process_line(line);
    }

    return 0;
}

void process_line(const std::string &line) {
    double score;

    int semicolon_pos = line.find(';');
    std::string cust_str = line.substr(0, semicolon_pos);
    std::string prod_str = line.substr(semicolon_pos + 1, std::string::npos);
    std::vector<std::string> customers = tokenize(cust_str, ',');
    std::vector<std::string> products = tokenize(prod_str, ',');

    int len = customers.size() >= products.size() ? customers.size() : products.size();
    int *scorei = new int[len * len];
    set_scores(scorei, len, products, customers);
    Hungarian hung(scorei, len);
    hung.init();
    score = scoreitodbl(hung.get_match_total());
    printf("%4.2f\n", score);
    delete[] scorei;
}

std::vector<std::string> tokenize(const std::string &rawtxt, const char &tok) {
    std::vector<std::string> tokens;
    int prev = 0,
        next;

    while ((next = rawtxt.find(tok, prev)) != std::string::npos) {
        tokens.push_back(rawtxt.substr(prev, next - prev));
        prev = next + 1;
    }
    tokens.push_back(rawtxt.substr(prev, std::string::npos));
    return tokens;
}

void set_scores(int *scorei, const int &len, const std::vector<std::string> &products, 
        const std::vector<std::string> &customers) {
    const int lensq = len * len,
        prod_len = products.size(),
        cust_len = customers.size();
    Index index(len);
    int i, j;

    std::fill(scorei, scorei + lensq, 0);
    for (i = 0; i < prod_len; ++i) {
        for (j = 0; j < cust_len; ++j) {
            scorei[index.index(i, j)] = get_scorei(products[i], customers[j]);
        }
    }
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
    return is_in(c, "aeiouy");
}

bool is_consonant(const char &c) {
    return is_in(c, "bcdfghjklmnpqrstvwxz");
}

bool is_letter(const char &c) {
    return 'a' <= c && c <= 'z';
}

int get_scorei(const std::string &product, const std::string &customer) {
    int prod_ltr_ct = count_letters(product),
        cust_ltr_ct = count_letters(customer);
    int multiple = relative_primes(prod_ltr_ct, cust_ltr_ct) ? 2 : 3;
    if (prod_ltr_ct % 2 == 0) {
        return multiple * 3 * count_vowels(customer);
    }
    return multiple * 2 * count_consonants(customer);
}

double scoreitodbl(const int &ss) {
    return ss / 4.0;
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

Index::Index(const int &cols) {
    cols_ = cols;
}

int Index::row(const int &index) const {
    return index / cols_;
}

int Index::col(const int &index) const {
    return index % cols_;
}

int Index::index(const int &row, const int &col) const {
    return row * cols_ + col;
}

MaxMatch::MaxMatch(const int *graph, const int &X_size, 
        const int &Y_size) : rows_(X_size), cols_(Y_size), index_(Y_size) {
    graph_ = new int[rows_ * cols_];
    match_by_X_ = new int[rows_];
    match_by_Y_ = new int[cols_];
    childX_ = new int[rows_];

    set(graph);
    reset();
}

MaxMatch::~MaxMatch() {
    delete[] childX_;
    delete[] match_by_Y_;
    delete[] match_by_X_;
    delete[] graph_;
}

// run the algorithm to get the matching
void MaxMatch::init() {
    int start_index;

    while ((start_index = dfs()) != -1) {
        augment_match(start_index);
    }
}
/**
 * get the column matched to a given row.
 * return -1 if no column matches
 */
int MaxMatch::match_X(const int &x) const {
    return match_by_X_[x];
}
/**
 * get the row matched to a given column.
 * return -1 if no row matches
 */
int MaxMatch::match_Y(const int &y) const {
    return match_by_Y_[y];
}

/**
 * reset the graph on which to find a matching
 * presupposes the same number of rows and
 * columns
 */
void MaxMatch::set(const int *graph) {
    int len = rows_ * cols_;

    for (int i = 0; i < len; ++i) {
        graph_[i] = graph[i] == 0 ? 0 : 1;
    }
    reset();
}

void MaxMatch::add_graph_edge(const int &x, const int &y) {
    graph_[index_.index(x, y)] = 1;
}

void MaxMatch::delete_graph_edge(const int &x, const int &y) {
    graph_[index_.index(x, y)] = 0;

}

bool MaxMatch::has_graph_edge(const int &x, const int &y) {
    return graph_[index_.index(x, y)] == 1;
}

void MaxMatch::reset() {
    reset_matches();
    reset_childX();
}

void MaxMatch::reset_matches() {
    std::fill(match_by_X_, match_by_X_ + rows_, -1);
    std::fill(match_by_Y_, match_by_Y_ + cols_, -1);
}

void MaxMatch::reset_childX() {
    std::fill(childX_, childX_ + rows_, -1);
}

int MaxMatch::dfs() {
    reset_childX();
    for (int i = 0; i < rows_; ++i) {
        if (match_by_X_[i] == -1 && dfs_visit(i)) {
            return i;
        }
    }
    return -1;
}

bool MaxMatch::dfs_visit(const int &i) {
    // vertex already visited
    if (childX_[i] >= 0) { return false; }
    for (int j = 0; j < cols_; ++j) {
        // we're only looking for unmatched edges
        if (graph_[index_.index(i, j)] == 0 || match_by_X_[i] == j) continue;
        childX_[i] = j;
        // j is unmatched, augmenting path found
        if (match_by_Y_[j] == -1) return true; 
        // j is matched, keep going
        if (dfs_visit(match_by_Y_[j])) return true;
    }
    childX_[i] = -1;
    return false;
}

void MaxMatch::augment_match(int i) {
    int nextX;

    while (i >= 0) {
        match_by_X_[i] = childX_[i];
        nextX = match_by_Y_[match_by_X_[i]];
        match_by_Y_[match_by_X_[i]] = i;
        i = nextX;
    }
}

int MaxMatch::matches() const {
    return std::count_if(match_by_X_, match_by_X_ + rows_, [](int x) { return x != -1; });
}

int MaxMatch::sizeX() const {
    return rows_;
}

int MaxMatch::sizeY() const {
    return cols_;
}

Hungarian::Hungarian(const int *weights, const int &len) : 
        len_(len), len_sq_(len_ * len_), index_(len_), matcher_(weights, len_, len_) {
    int i;

    // initialize weights
    weights_ = new int[len_sq_];
    for (i = 0; i < len_sq_; ++i) {
        weights_[i] = weights[i];
    }
    // initialize vertex labels
    labelsX_ = new int[len_];
    labelsY_ = new int[len_];
    for (i = 0; i < len_; ++i) {
        labelsX_[i] = *std::max_element(weights_ + index_.index(i, 0), 
                weights_ + index_.index(i + 1, 0));
        labelsY_[i] = 0;
    }
    //initialize equality graph to starting values
    equality_graph_ = new int[len_sq_];
    update_equality_graph();
    // set matcher to initial equality graph
    matcher_.set(equality_graph_);
    matcher_.init();
    // initialize S_, T_, NlS_
    S_ = new int[len_];
    T_ = new int[len_];
    NlS_ = new int[len_];
}
Hungarian::~Hungarian() {
    delete[] weights_;
    delete[] labelsX_;
    delete[] labelsY_;
    delete[] equality_graph_;
    delete[] S_;
    delete[] T_;
    delete[] NlS_;
}

int Hungarian::get_match_total() {
    int total = 0;

    for (int i = 0; i < len_; ++i) {
        if (matcher_.match_X(i) >= 0) {
            total += weights_[index_.index(i, matcher_.match_X(i))];
        }
    }
    return total;
}

void Hungarian::init() {
    while (matcher_.matches() < len_) {
        improve_equality_graph();
        matcher_.set(equality_graph_);
        matcher_.init();
    }
}

int Hungarian::length() const {
    return len_;
}

int Hungarian::weight(const int &x, const int &y) const {
    return weights_[index_.index(x, y)];
}

int Hungarian::matchX(const int &x) const {
    return matcher_.match_X(x);
}

int Hungarian::matchY(const int &y) const {
    return matcher_.match_Y(y);
}

void Hungarian::improve_equality_graph() {
    reset_path_sets();
    int free_vertex = get_free_vertex();
    S_[free_vertex] = 1;
    update_NlS(free_vertex);
    int y = nls_minus_t();
    while (y >= 0) {
        T_[y] = 1;
        S_[matcher_.match_Y(y)] = 1;
        update_NlS(matcher_.match_Y(y));
        y = nls_minus_t();
    }
    relabel();
    update_equality_graph();
}

int Hungarian::get_free_vertex() const {
    for (int i = 0; i < len_; ++i) {
        if (matcher_.match_X(i) < 0) return i; 
    }
    return -1;
}

void Hungarian::update_equality_graph() {
    int i, j;

    for (i = 0; i < len_; ++i) {
        for (j = 0; j < len_; ++j) {
            if (labelsX_[i] + labelsY_[j] == weights_[index_.index(i, j)]) {
                equality_graph_[index_.index(i, j)] = 1;
            } else {
                equality_graph_[index_.index(i, j)] = 0;
            }
        }
    }
}

int Hungarian::get_alpha() const {
    int alpha = -1,
        i,
        j;

    for (i = 0; i < len_; ++i) {
        for (j = 0; j < len_; ++j) {
            if (S_[i] == 1 && T_[j] == 0) {
                if (alpha == -1 || labelsX_[i] + labelsY_[j] - weights_[index_.index(i, j)] < alpha) {
                    alpha = labelsX_[i] + labelsY_[j] - weights_[index_.index(i, j)];
                }
            }
        }
    }
    return alpha;
}

void Hungarian::reset_path_sets() {
    std::fill(S_, S_ + len_, 0);
    std::fill(T_, T_ + len_, 0);
    std::fill(NlS_, NlS_ + len_, 0);
}

/**
 * Add the neighbors of input vertex in the equality
 * graph to NlS
 */
void Hungarian::update_NlS(const int &vertex) {
    for (int j = 0; j < len_; ++j) {
        if (equality_graph_[index_.index(vertex, j)] == 1) {
            NlS_[j] = 1;
        }
    }
}

/**
 * return some vertex in NlS that isn't in T.
 * return -1 if there is no such vertex (NlS_ == T_)
 */
int Hungarian::nls_minus_t() const {
    for (int i = 0; i < len_; ++i) {
        if (NlS_[i] == 1 && T_[i] == 0) return i;
    }
    return -1;
}

void Hungarian::relabel() {
    int alpha = get_alpha(),
        i;

    for (i = 0; i < len_; ++i) {
        if (S_[i] == 1) {
            labelsX_[i] -= alpha;
        }
        if (T_[i] == 1) {
            labelsY_[i] += alpha;
        }
    }

}
