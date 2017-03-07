from distutils.core import setup

setup(
  name = 'table-extractor',
  packages = ['table_extractor'],
  package_dir = {'table_extractor': 'table_extractor'},
  package_data = {'table_extractor': ['__init__.py']},
  version = '0.7',
  description = 'Extract normalized tables from CSVs, Excel Spreadsheets, PDFs, Word Docs, and Web Pages',
  author = 'Daniel J. Dufour',
  author_email = 'daniel.j.dufour@gmail.com',
  url = 'https://github.com/DanielJDufour/table-extractor',
  download_url = 'https://github.com/DanielJDufour/table-extractor/tarball/download',
  keywords = ['table', 'python'],
  classifiers = [],
)
