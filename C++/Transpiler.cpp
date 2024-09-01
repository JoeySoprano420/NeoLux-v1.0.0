#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <stdexcept>

// Helper function to trim whitespace from strings
std::string trim(const std::string& str) {
    size_t start = str.find_first_not_of(" \t\n\r");
    size_t end = str.find_last_not_of(" \t\n\r");
    return (start == std::string::npos || end == std::string::npos) ? "" : str.substr(start, end - start + 1);
}

// Function to translate Neolux code to C++ code
std::string translate_neolux_to_cpp(const std::string& neolux_code) {
    std::istringstream stream(neolux_code);
    std::ostringstream cpp_code;
    std::string line;
    bool inside_function = false;
    bool inside_main = false;
    std::string current_function;

    cpp_code << "#include <iostream>\n#include <vector>\n#include <string>\n\n";

    while (std::getline(stream, line)) {
        line = trim(line);

        // Skip comments
        if (line.find("+") != std::string::npos) {
            continue;
        }

        // Translate function definitions
        if (line.find("function") != std::string::npos) {
            if (inside_function) {
                throw std::runtime_error("Unexpected function definition inside another function.");
            }
            size_t pos = line.find("function");
            std::string func_name = trim(line.substr(pos + 9, line.find("(", pos) - pos - 9));
            cpp_code << "void " << func_name << "(";
            current_function = func_name;
            inside_function = true;
        }
        // Handle function parameters
        else if (inside_function && line.find(")") != std::string::npos) {
            cpp_code << ") {\n";
            inside_function = false;
        }
        // Handle function end
        else if (line.find("end") != std::string::npos) {
            if (!inside_function) {
                cpp_code << "\n}\n\n";
            } else {
                throw std::runtime_error("Mismatched function end.");
            }
        }
        // Handle let statements (variable declarations)
        else if (line.find("let") != std::string::npos) {
            size_t pos = line.find("let");
            std::string variable_declaration = trim(line.substr(pos + 4));
            if (variable_declaration.find('=') != std::string::npos) {
                cpp_code << "    " << variable_declaration << ";\n";
            } else {
                cpp_code << "    std::vector<std::string> " << variable_declaration << ";\n";
            }
        }
        // Handle for loops
        else if (line.find("for") != std::string::npos) {
            size_t pos = line.find("for");
            std::string loop_part = trim(line.substr(pos + 4));
            cpp_code << "    for (const auto& " << loop_part << ") {\n";
        }
        // Handle print statements
        else if (line.find("print") != std::string::npos) {
            size_t pos = line.find("print");
            std::string print_statement = trim(line.substr(pos + 6, line.find(")", pos) - pos - 6));
            cpp_code << "        std::cout << " << print_statement << " << std::endl;\n";
        }
        // Handle main function call
        else if (line.find("main()") != std::string::npos) {
            if (inside_main) {
                throw std::runtime_error("Multiple main function calls are not supported.");
            }
            cpp_code << "int main() {\n";
            inside_main = true;
        }
        else if (inside_main && line.empty()) {
            cpp_code << "    return 0;\n";
            cpp_code << "}\n";
            inside_main = false;
        }
    }

    if (inside_main) {
        cpp_code << "    return 0;\n";
        cpp_code << "}\n";
    }

    return cpp_code.str();
}

int main() {
    std::string neolux_code = R"(
+ This is a comment +

function greet(name) ~
    print("Hello, ", name) *
end +

function main() ~
    let names = ["Alice", "Bob", "Charlie"] *
    for name in names ~
        greet(name) *
    end ~
end +

main() *
)";

    try {
        std::string cpp_code = translate_neolux_to_cpp(neolux_code);
        std::cout << cpp_code << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
