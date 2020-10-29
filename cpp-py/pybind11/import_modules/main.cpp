#include <pybind11/embed.h>
#include <iostream>

namespace py = pybind11;

int main() {
    py::scoped_interpreter guard{};

    py::module calc = py::module::import("calc");
    py::object result = calc.attr("add")(1, 2);
    int n = result.cast<int>();
    std::cout << "Computed sum: " << n << std::endl;
    assert(n == 3);
}
