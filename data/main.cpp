#include <bits/stdc++.h>
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>

using namespace std;

inline std::vector<std::string> read_input(const std::string& file_name) {
    std::ifstream in(file_name);
    if (!in.is_open()) {
        throw std::runtime_error("Impossible d'ouvrir " + file_name);
    }
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(in, line)) {
        if (!line.empty() && line.back() == '\r') line.pop_back();
        lines.push_back(line);
    }
    return lines;
}

auto part1() -> long long {
    // TODO: logique partie 1
    string inputName = "input_part1.txt";
    auto lines = read_input(inputName);
    return 0;
}

auto part2() -> long long {
    // TODO: logique partie 2
    string inputName = "input_part2.txt";
    auto lines = read_input(inputName);
    return 0;
}

int main() {
    cout << "Part 1: " << part1() << "\n";
    cout << "Part 2: " << part2() << "\n";
    return 0;
}

