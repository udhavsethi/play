cmake_minimum_required(VERSION 3.7)
project(calculator)

find_package(pybind11 REQUIRED)  # or add_subdirectory(pybind11)

add_executable(calculator main.cpp)
target_link_libraries(calculator PRIVATE pybind11::embed)
