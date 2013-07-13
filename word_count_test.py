#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
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
        test_text = ("In a hole in the ground there lived a Hobbit"
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

    def test_read_filename(self):
        '''read the file name into a hash'''
        self.create_test_file()
        self.delete_test_file()

    def test_count_frequency(self):
        self.test_count.count_frequency("crocodile")
        self.test_count.count_frequency("crocodile")
        self.assertEqual(2, self.test_count.word_log.get("crocodile"))

    def test_process_line(self):
        self.test_count.process_line("!giraffe!!! giraffe! giraffe")
        self.assertEqual(3, self.test_count.word_log.get("giraffe"))

        


if __name__ == '__main__':
    unittest.main()


