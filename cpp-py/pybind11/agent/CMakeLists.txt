cmake_minimum_required(VERSION 3.7)
project(agent)

find_package(pybind11 REQUIRED)  # or add_subdirectory(pybind11)

add_executable(agent invoke_agent.cpp)
target_link_libraries(agent PRIVATE pybind11::embed)
