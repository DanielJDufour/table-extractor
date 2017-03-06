#-*- coding: utf-8 -*-
import signal, unittest
from datetime import datetime
from inspect import getargspec
from table_extractor import *
from os.path import abspath, dirname, realpath
from requests import get

path_to_directory_of_this_file = dirname(realpath(__file__))

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise OSError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

class TestMethods(unittest.TestCase):

    def testFormats(self):
        for _format in ("csv", "tsv", "xlsx"):
            try:
                tables = extract_tables(path_to_directory_of_this_file + "/test." + _format)
                self.assertEqual(len(tables), 1)
                self.assertEqual(len(tables[0]), 11)
            except Exception as e:
                print "CAUGHT ERROR on format:", _format, e


if __name__ == '__main__':
    unittest.main()
