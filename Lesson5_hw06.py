import string
tuple_line = tuple (dir (string)) [:5]
print ('tuple_line1:', tuple_line)
list_line = list(tuple_line)
list_line.insert(2,'capwords')
print ('tuple_lin2:', tuple (list_line)