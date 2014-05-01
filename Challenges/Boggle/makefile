# Copyright (c) 2014 Marshall Farrier
# license http://opensource.org/licenses/gpl-license.php GNU Public License
#
# makefile for boggle solver
# author Marshall Farrier
# since 2014-04-29

# For makefile structure cf.
# http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/

CC=gcc
BINDIR=./bin

trie_test: trie_test.o trie.o
	$(CC) -o $(BINDIR)/trie_test trie_test.o trie.o

trie_test.o: trie_test.c trie.h
	gcc -c trie_test.c

trie.o: trie.c trie.h
	gcc -c trie.c

.PHONY: clean
clean:
	rm *.o *~ $(BINDIR)/*
