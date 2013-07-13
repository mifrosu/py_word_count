#!/usr/bin/env python
# -*- coding: utf-8 -*-
# written by Michael O'Sullivan (mifrosu@gmail.com)

from __future__ import print_function
from __future__ import with_statement

import word_count as wc
import unittest
import os

class WordCountTest(unittest.TestCase):

    def setUp(self):
        self.file_name = "test_file.txt"
        self.test_count = wc.WordCount(self.file_name)

    def create_test_file(self):
        ''' we will create a test file with some text '''
        test_text = ("In a hole in the ground there lived a Hobbit. "
                     "Not a nasty, dirty, wet hole, filled with the ends "
                     "of worms and an oozy smell, nor yet a dry, bare, "
                     "sandy hole with nothing in it to sit down on or to"
                     "eat: it was a hobbit-hole, and that means comfort"
                     ".\n")
        with open(self.file_name, 'wt') as output:
            output.write(test_text)

    def delete_test_file(self):
        os.remove(self.file_name)

    def test_init_filename(self):
        '''the class should initialize with a file name and default n'''
        self.assertEqual("test_file.txt", self.test_count.file_name)
        self.assertEqual(-1, self.test_count.n)

    def test_init_filename_n(self):
        '''initialize class with file name and n values'''
        test_count = wc.WordCount("a_file.txt", 29)
        self.assertEqual("a_file.txt", test_count.file_name)
        self.assertEqual(29, test_count.n)

    def test_count_frequency(self):
        self.test_count.count_frequency("crocodile")
        self.test_count.count_frequency("crocodile")
        self.assertEqual(2, self.test_count.word_log.get("crocodile"))

    def test_process_line(self):
        '''check for punctuation removal and case change'''
        self.test_count.process_line("!giraffe!!! giraffe! Giraffe")
        self.assertEqual(3, self.test_count.word_log.get("giraffe"))
        
    def test_process_file(self):
        self.create_test_file()
        self.test_count.process_file()
        self.assertEqual(3, self.test_count.word_log.get("hole"))
        self.delete_test_file()

    def test_process_file_ioerror(self):
        '''file does not exist'''
        print("\nNow testing for IOError: we should see an error msg->")
        self.assertRaises(IOError, self.test_count.process_file)

    def test_generate_stats(self):
        self.test_count.process_line("to be or not to be")
        self.test_count.generate_stats()
        self.assertEqual([("be", 2), ("to", 2), ("not", 1), ("or", 1)],
                         self.test_count.stats_tuple_list)
        #self.test_count.print_stats(self.test_count.stats_tuple_list)


if __name__ == '__main__':
    unittest.main()


