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

    def testDoc(self):
        try:
            tables = extract_tables(path_to_directory_of_this_file + "/test.docx")
            self.assertEqual(len(tables), 1)
        except Exception as e:
            print "Caught EXCEPTION on docx:", e

    def testFormats(self):
        for _format in ("csv", "tsv", "xlsx"):
            try:
                tables = extract_tables(path_to_directory_of_this_file + "/test." + _format)
                self.assertEqual(len(tables), 1)
                self.assertEqual(len(tables[0]), 10)
            except Exception as e:
                print "CAUGHT ERROR on format:", _format, e

    def testHTML(self):
        try:
            html = get("http://www.nuforc.org/webreports/ndxlAK.html").text
            tables = extract_tables(html)
            self.assertEqual(len(tables), 1)
            self.assertTrue(len(tables[0]) > 50)
        except Exception as e:
            print "CAUGHT EXCEPTION in te4stHTML:", e

    def testWebpage(self):
        tables = extract_tables("http://www.nuforc.org/webreports/ndxlAK.html")
        try:
            self.assertEqual(len(tables), 1)
            self.assertTrue(len(tables[0]) > 50)
        except Exception as e:
            print "CAUGHT ERROR testWebpage:", e


if __name__ == '__main__':
    unittest.main()
