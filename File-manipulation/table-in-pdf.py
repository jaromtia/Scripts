import camelot

tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)

tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')


# TODO: allow user input to pull from specific pdf page
# TODO: allow user input for file output name
# TODO: turn this more into a command-line tool with flags as specific options