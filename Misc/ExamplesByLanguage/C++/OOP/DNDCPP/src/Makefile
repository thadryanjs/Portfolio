CC = g++
CFLAGS = -g -Wall -I $(INC_DIR) -I $(INC_DIR2)
SRC = ddcpp.cpp
INC_DIR = models
INC_DIR2 = types
all: ddcpp

ddcpp: ddcpp.cpp
	$(CC) $(CFLAGS) -o ddcpp ddcpp.cpp
clean:
	rm ddcpp
