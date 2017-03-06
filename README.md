[![Build Status](https://travis-ci.org/DanielJDufour/table-extractor.svg?branch=master)](https://travis-ci.org/DanielJDufour/table-extractor)


# table-extractor
Extract normalized tables from CSVs, Excel Spreadsheets, Word Docs, and Web Pages

A table is basically a list of rows.  And a row is basically a list of values.

# Installation
```
pip install table-extractor
```

# Use
```
from table_extractor import extract_tables
tables = extract_tables("/tmp/top_5_movies.docx")
# [[["Name", "Rating"], ["The Shawshank Redemption", 9.2], ["The Godfather", 9.2], ["The Godfather: Part II", 9.2], ["The Dark Knight", 8.9], ["12 Angry Men", 8.9]]]
```
# Testing
To test the package run
```
python -m unittest table_extractor.tests.test
```
