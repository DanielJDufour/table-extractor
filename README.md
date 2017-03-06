[![Build Status](https://travis-ci.org/DanielJDufour/table-extractor.svg?branch=master)](https://travis-ci.org/DanielJDufour/table-extractor)


# table-extractor
Extract normalized tables from CSVs, Excel Spreadsheets, Word Docs, and Web Pages

# Installation
```
pip install table-extractor
```

# Use
```
from table_extractor import extract_tables
tables = extract_tables(text)
```
# Testing
To test the package run
```
python -m unittest table_extractor.tests.test
```
