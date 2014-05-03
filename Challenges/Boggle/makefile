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

.PHONY: all
all: tst_trie tst_list

# list
tst_list: tst_list.o list.o
	$(CC) -o $(BINDIR)/tst_list tst_list.o list.o $(CFLAGS)

tst_list.o: tst_list.c 
	gcc -c tst_list.c $(CFLAGS)

list.o: list.c
	gcc -c list.c $(CFLAGS)
	
# trie
tst_trie: tst_trie.o trie.o
	$(CC) -o $(BINDIR)/tst_trie tst_trie.o trie.o $(CFLAGS)

tst_trie.o: tst_trie.c 
	gcc -c tst_trie.c $(CFLAGS)

trie.o: trie.c
	gcc -c trie.c $(CFLAGS)

.PHONY: clean
clean:
	rm -f *.o *~ $(BINDIR)/*
