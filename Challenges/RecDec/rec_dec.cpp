/**
 * Template from Skiena et al., Programming Challenges, p. 8
 * for standard input/output
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2015-03-22
 *
 * https://leetcode.com/problems/fraction-to-recurring-decimal/
 */

#include <algorithm>
#include <climits>
#include <list>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Solution {
private:
    list<unsigned int> *remainders;
    static constexpr int maxplaces = 2048;
    static constexpr unsigned int NUM_LIMIT = UINT_MAX / 10;
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (denominator == 0) { return "wrong! 0 denominator"; }
        if (numerator == 0) { return "0"; }
        bool isnegative = (numerator < 0 != denominator < 0);
        unsigned int num = numerator >= 0 ? numerator : -numerator;
        unsigned int denom = denominator >= 0 ? denominator : -denominator;
        unsigned int whole = num / denom;
        unsigned int fraction = num % denom;
        ostringstream convert;
        if (isnegative) {
            convert << '-';
        }
        convert << whole;
        if (fraction != 0) {
            remainders = new list<unsigned int>();
            convert << '.' << get_dec(fraction, denom);
            delete remainders;
        }
        return convert.str();
    }

    string get_dec(const unsigned int &num, const unsigned int &denom) {
        // num and denom are guaranteed to be positive
        ostringstream convert;
        unsigned int vals[2];
        rec_dec(convert, num, denom, 0, vals);
        return convert.str();
    }

    void rec_dec(ostringstream &prev, const unsigned int &num, const unsigned int &denom, const int &places, unsigned int vals[]) {
        if (places > maxplaces) { return; }
        set_next(num, denom, vals);
        unsigned int nextdig = vals[0];
        unsigned int remainder = vals[1];
        if (remainder == 0) { 
            prev << nextdig;
            return; 
        }
        if (remainders->size() > 0) {
            list<unsigned int>::iterator it = find(remainders->begin(), remainders->end(), remainder);
            if (it != remainders->end()) {
                insert_parens(prev, it, nextdig);
                return;
            }
        }
        prev << nextdig;
        remainders->push_back(remainder);
        rec_dec(prev, remainder, denom, places + 1, vals);
    }

    void insert_parens(ostringstream &prev, const list<unsigned int>::iterator &ref_it, const unsigned int &curr_dec) {
        string current = prev.str();
        size_t pos = 0;
        list<unsigned int>::iterator it = remainders->begin();
        while (it++ != ref_it) { ++pos; }
        if (current[pos] != '0' + curr_dec) {
            prev << curr_dec;
            ++pos;
            current = prev.str();
        }
        current.insert(pos, "(");
        prev.str("");
        prev.clear();
        prev << current << ')';
    }

    void set_next(const unsigned int &num, const unsigned int &denom, unsigned int *vals) {
        const unsigned int max = denom - num;
        // vals[0] is quotient, vals[1] is remainder
        vals[0] = 0;
        vals[1] = 0;
        for (unsigned int i = 0; i < 10; ++i) {
            if (vals[1] >= max) {
                vals[1] -= max;
                ++vals[0];
            }
            else {
                vals[1] += num;
            }
        }
    }
};

int main() {
    int numerator, denominator;
    std::string line;
    std::istringstream iss;

    while (std::getline(std::cin, line)) {
        iss.clear();
        iss.str(line);
        iss >> numerator >> denominator;
        Solution sol;
        std::cout << sol.fractionToDecimal(numerator, denominator) << endl;
    }

    return 0;
}
