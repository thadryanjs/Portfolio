#
# Makefile for the Free Software Foundations g++ compiler
#
CC = g++
CFLAGS = -g -Wall -I $(INC_DIR)
SRC = ddcpp.cpp
INC_DIR = src	
all: ddcpp

ddcpp: ddcpp.cpp
	$(CC) $(CFLAGS) -o ddcpp ddcpp.cpp
clean:
	rm ddcpp
