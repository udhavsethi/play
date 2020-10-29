g++ -c func.cpp -o func.o -fPIC $(/usr/bin/python3.8-config --cflags)
g++ func.o -o func $(/usr/bin/python3.8-config --embed --ldflags)
