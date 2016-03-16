/**
 * Determine the highest score in each of several categories.
 * https://www.codeeval.com/open_challenges/208/
 *
 * Copyright (c) 2016 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2016-03-16
 */

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void show_high(const std::string &line);
std::vector<std::vector<int> > parse_line(const std::string &line);
std::vector<int> parse_token(const std::string &token);
std::vector<int> get_highs(const std::vector<std::vector<int> > &table);

int main(int argc, char *argv[]) {
    std::ifstream stream(argv[1]);
    std::string line;

    while (std::getline(stream, line)) {
        show_high(line);
        std::cout << std::endl;
    }
    return 0;
}

void show_high(const std::string &line) {
    std::vector<std::vector<int> > table = parse_line(line);
    std::vector<int> highs = get_highs(table);
    bool first_time = true;
    for (int high : highs) {
        if (first_time) {
            first_time = false;
        } else {
            std::cout << ' ';
        }
        std::cout << high;
    }
}

std::vector<int> get_highs(const std::vector<std::vector<int> > &table) {
    std::vector<int> highs(table[0]);
    const size_t n_rows = table.size();
    const size_t n_cols = highs.size();
    for (size_t i = 1; i < n_rows; ++i) {
        for (size_t j = 0; j < n_cols; ++j) {
            if (table[i][j] > highs[j]) {
                highs[j] = table[i][j];
            }
        }
    }
    return highs;
}

std::vector<std::vector<int> > parse_line(const std::string &line) {
    std::vector<std::vector<int> > table;
    size_t end = 0;
    size_t begin = 0;
    const std::string separator(" | ");
    const size_t sep_len = separator.length();
    while ((end = line.find(separator, begin)) != std::string::npos) {
        table.push_back(parse_token(line.substr(begin, end - begin)));
        begin = end + sep_len;
    }
    table.push_back(parse_token(line.substr(begin, end - begin)));
    return table;
}

std::vector<int> parse_token(const std::string &token) {
    std::vector<int> row;
    size_t end = 0;
    size_t begin = 0;
    const std::string separator(" ");
    const size_t sep_len = separator.length();
    while ((end = token.find(separator, begin)) != std::string::npos) {
        row.push_back(std::stoi(token.substr(begin, end - begin)));
        begin = end + sep_len;
    }
    row.push_back(std::stoi(token.substr(begin, end - begin)));
    return row;
}
