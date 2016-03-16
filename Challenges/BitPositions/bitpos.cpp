/**
 * Determine whether or not 2 bits in a number are the same.
 * https://www.codeeval.com/open_challenges/19/
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2016-03-15
 */

#include <climits>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

class Solver {
    private:
        std::vector<int> powers_of_two;
        std::vector<int> parse_line(const std::string &line);
    public:
        Solver();
        std::string solve(const std::string &line);
};

int main(int argc, char *argv[]) {
    std::ifstream stream(argv[1]);
    std::string line;
    Solver solver;

    while (std::getline(stream, line)) {
        std::cout << solver.solve(line) << std::endl;
    }
    return 0;
}

Solver::Solver() {
    int val = 1;
    int max = INT_MAX / 2;
    while (val <= max) {
        powers_of_two.push_back(val);
        val *= 2;
    }
    powers_of_two.push_back(val);
}

std::string Solver::solve(const std::string &line) {
    std::vector<int> vals = parse_line(line);
    if (!(vals[0] & powers_of_two[vals[1] - 1]) != !(vals[0] & powers_of_two[vals[2] - 1])) {
        return "false";
    }
    return "true";
}

std::vector<int> Solver::parse_line(const std::string &line) {
    std::vector<int> vals;
    size_t end = 0;
    size_t begin = 0;
    while ((end = line.find(',', begin)) != std::string::npos) {
        vals.push_back(std::stoi(line.substr(begin, end - begin)));
        begin = end + 1;
    }
    vals.push_back(std::stoi(line.substr(begin, end - begin)));
    return vals;
}
