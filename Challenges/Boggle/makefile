# Copyright (c) 2014 Marshall Farrier
# license http://opensource.org/licenses/gpl-license.php GNU Public License
#
# makefile for boggle solver
# author Marshall Farrier
# since 2014-04-29

# For makefile structure cf.
# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/

#main: main.c trie.c
#	gcc -Wall main.c trie.c -o bin/main -I.

main: main.o trie.o
	gcc -o bin/main main.o trie.o

main.o: main.c trie.h
	gcc -c main.c

trie.o: trie.c trie.h
	gcc -c trie.c
