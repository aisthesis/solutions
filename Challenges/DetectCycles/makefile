# Call using program name as argument.
# Example:
# > make hello
# This command will compile 'src/hello.c' and create
# an executable file, 'hello'
#
# Copyright (c) 2014 Marshall Farrier
# license http://opensource.org/licenses/gpl-license.php GNU Public License
# 
# Author Marshall Farrier
# since 2014-05-03

# For C
# CC = gcc
# EXT = c
# For C++
CC = g++
EXT = cpp

.PHONY: all
all: directories %

.PHONY: directories
directories: 
	mkdir -p bin

%: %.$(EXT)
	$(CC) -Wall $< -o bin/$@
