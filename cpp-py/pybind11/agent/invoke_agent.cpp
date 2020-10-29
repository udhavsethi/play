#include <pybind11/embed.h>
#include <iostream>
#include <pybind11/stl.h>


namespace py = pybind11;

int main() {
	int length = 309;
	std::vector<double> event_snapshot(length, 0.0);

    py::scoped_interpreter guard{};
    py::module agent = py::module::import("agent");
    py::object action = agent.attr("run_inference")(event_snapshot);
    int a = action.cast<int>();
    std::cout << "Chosen action: " << a << std::endl;
}
