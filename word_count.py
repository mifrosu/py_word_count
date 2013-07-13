#!/usr/bin/env python
from __future__ import print_function
from __future__ import with_statement
from __future__ import unicode_literals

import re

# Q. Write a program, preferably in Python, that given a text file, counts the
# number of words and reports the top N words ordered by the number of times 
# they appear in the file.

# As well as seeing an answer, I'd also appreciate a note on how long the 
# program took to write, and a summary of any research done.

# 11.30

class WordCount(object):

    def __init__(self, file_name, n=-1):
        self.file_name = file_name
        self.n = n if n > 0 else -1
        self.word_log = {}

    def count_frequency(self, word):
        '''add to a word frequency dict hash table'''
        self.word_log[word] = self.word_log.get(word,0) + 1

    def process_line(self, line):
        temp_list = line.split()
        # check if words feature a non-alphanumeric char at either end,
        # e.g. Spanish usage, remove char if present
        check = re.compile("\W")
        for i in range(0,len(temp_list)):
            while check.search(temp_list[i]) != None:
                k = check.search(temp_list[i])
                if k and k.start() != 0:
                    temp_list[i] = temp_list[i][:k.start()] 
                elif k and  k.start() == 0:
                    temp_list[i] = temp_list[i][1:]
            print(temp_list[i])
            self.count_frequency(temp_list[i])

    def process_file(self):
        try:
            with open(self.file_name) as in_file:
                for line in in_file:
                    self.process_line(line)
        except IOError:
            print("There was a problem processing the file.")











        

        



def main():
    print("This will count files.")

if __name__ == '__main__':
    main()
