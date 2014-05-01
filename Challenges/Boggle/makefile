# Copyright (c) 2014 Marshall Farrier
# license http://opensource.org/licenses/gpl-license.php GNU Public License
#
# makefile for boggle solver
# author Marshall Farrier
# since 2014-04-29

# For makefile structure cf.
# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/

CC=gcc
CFLAGS=-I.
BINDIR=./bin

trie_test: trie_test.o trie.o
	$(CC) -o $(BINDIR)/trie_test trie_test.o trie.o $(CFLAGS)

trie_test.o: trie_test.c 
	gcc -c trie_test.c $(CFLAGS)

trie.o: trie.c
	gcc -c trie.c $(CFLAGS)

.PHONY: clean
clean:
	rm -f *.o *~ $(BINDIR)/*
