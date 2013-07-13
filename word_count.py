#!/usr/bin/env python
# -*- coding: utf-8 -*-
# written by Michael O'Sullivan (mifrosu@gmail.com)

from __future__ import print_function
from __future__ import with_statement

import argparse
import re
from operator import itemgetter

class WordCount(object):

    def __init__(self, file_name, n=-1):
        self.file_name = file_name
        self.n = n if n > 0 else -1
        self.word_log = {}
        self.stats_tuple_list = []

    def count_frequency(self, word):
        '''reads/creates and increments word_log entry'''
        self.word_log[word] = self.word_log.get(word,0) + 1

    def process_line(self, line):
        '''removes punctuation (inc. prefixes) and calls count_frequency'''
        temp_list = line.lower().split()
        check = re.compile("\W")
        for i in range(0,len(temp_list)):
            while check.search(temp_list[i]) != None:
                k = check.search(temp_list[i])
                if k.start() != 0:
                    temp_list[i] = temp_list[i][:k.start()] 
                elif k.start() == 0:
                    temp_list[i] = temp_list[i][1:]
            self.count_frequency(temp_list[i])

    def process_file(self):
        try:
            with open(self.file_name) as in_file:
                for line in in_file:
                    self.process_line(line)
        except IOError:
            print("There was a problem processing {0}".format(self.file_name))
            raise

    def generate_stats(self):
        '''Creates a list of tuples from {'key': value}
        
        The list is sorted alphabetically by 'key', then descending
        by value.
        '''
        self.stats_tuple_list = self.word_log.items()
        self.stats_tuple_list.sort()
        self.stats_tuple_list.sort(key=itemgetter(1), reverse=True)

    def print_stats(self, in_tuple_list):
        max_digits = len(str(in_tuple_list[0][1])) 
        for i in in_tuple_list:
            print("{1: >{0}} {2}".format(max_digits+1, i[1], i[0]))

    def print_stats_range(self):
        if self.n < 1 or self.n > len(self.stats_tuple_list):
            self.print_stats(self.stats_tuple_list)
        else:
            self.print_stats(self.stats_tuple_list[:self.n])

    def run(self):
        self.process_file()
        self.generate_stats()
        self.print_stats_range()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", 
                        help="Get entire word frequency list")
    parser.add_argument("-n", "--number", type=int,
                        help="Specify top n word frequencies to view. " 
                        "If n is less than 1 or greater than the number "
                        "of words in the frequency list, the entire "
                        "word frequency list is printed.")
    args = parser.parse_args()
    if args.file_name and args.number:
        main_count = WordCount(args.file_name, args.number)
    elif args.file_name:
        main_count = WordCount(args.file_name) 
    if main_count:
        main_count.run()


if __name__ == '__main__':
    main()
