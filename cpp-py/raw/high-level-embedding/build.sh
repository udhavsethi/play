## for c
# gcc -c date.c -o date.o -fPIC $(/usr/bin/python3.8-config --cflags)
# gcc date.o -o date $(/usr/bin/python3.8-config --embed --ldflags)

## for cpp
g++ -c date.cpp -o date.o -fPIC $(/usr/bin/python3.8-config --cflags)
g++ date.o -o date $(/usr/bin/python3.8-config --embed --ldflags)
