#pragma once
#include <fstream>
#include <string>
#include <vector>
#include <stdexcept>

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
