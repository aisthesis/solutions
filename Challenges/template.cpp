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

int main() {
    int a;
    std::string line;
    std::istringstream iss;

    while (std::getline(std::cin, line)) {
        iss.clear();
        iss.str(line);
        iss >> a;
        std::cout << a << std::endl;
        
    }

    return 0;
}
